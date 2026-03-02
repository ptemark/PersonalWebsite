#!/bin/bash
#
# RALPH - Recursive Autonomous Loop for Project Handling
#
# Runs Claude Code in autonomous mode, continuously working through
# tasks defined in RALPH.md and tracked in spec/TASKS.md.
#
# Usage:
#   ./ralph.sh              # Run full loop
#   ./ralph.sh --once       # Run single iteration
#   ./ralph.sh --dry-run    # Show what would be executed
#   ./ralph.sh --verbose    # Stream output live
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RALPH_PROMPT="$SCRIPT_DIR/RALPH.md"

# Configuration
MAX_ITERATIONS=50
ITERATION_DELAY=5
LOG_DIR="$SCRIPT_DIR/logs"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Flags
SINGLE_RUN=false
DRY_RUN=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --once)
            SINGLE_RUN=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [--once] [--dry-run] [--verbose] [-h|--help]"
            echo ""
            echo "Options:"
            echo "  --once       Run single iteration (no loop)"
            echo "  --dry-run    Show what would be executed without running"
            echo "  --verbose    Stream live output during execution"
            echo "  -h, --help   Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

mkdir -p "$LOG_DIR"

# Patterns that indicate secrets in staged or tracked files
SECRET_PATTERNS=(
    'api[_-]?key\s*[:=]'
    'api[_-]?secret\s*[:=]'
    'access[_-]?token\s*[:=]'
    'secret[_-]?key\s*[:=]'
    'private[_-]?key\s*[:=]'
    'password\s*[:=]'
    'passwd\s*[:=]'
    'auth[_-]?token\s*[:=]'
    'bearer\s+'
    'AKIA[0-9A-Z]{16}'
    'ghp_[0-9a-zA-Z]{36}'
    'github[_-]token\s*[:=]'
)

log()     { echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"; }
success() { echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')] ✓${NC} $1"; }
warn()    { echo -e "${YELLOW}[$(date '+%Y-%m-%d %H:%M:%S')] ⚠${NC} $1"; }
error()   { echo -e "${RED}[$(date '+%Y-%m-%d %H:%M:%S')] ✗${NC} $1"; }

# Scan tracked and staged files for secret patterns
scan_for_secrets() {
    log "Scanning for secrets in staged/tracked files..."
    local found=0

    for pattern in "${SECRET_PATTERNS[@]}"; do
        local matches
        matches=$(git diff --cached --unified=0 2>/dev/null | grep -iE "$pattern" || true)
        if [[ -n "$matches" ]]; then
            error "POSSIBLE SECRET DETECTED in staged changes (pattern: $pattern)"
            error "$matches"
            found=1
        fi
    done

    if [[ $found -eq 1 ]]; then
        error "ABORTING: Secrets scan failed. Review staged files before committing."
        error "Run 'git diff --cached' to inspect what is staged."
        exit 1
    fi

    success "Secrets scan passed — no secrets detected in staged changes"
}

check_prerequisites() {
    log "Checking prerequisites..."

    if ! command -v claude &> /dev/null; then
        error "claude CLI not found. Install it from https://claude.ai/code"
        exit 1
    fi

    if ! command -v npm &> /dev/null; then
        error "npm not found. Please install Node.js."
        exit 1
    fi

    if [[ ! -f "$RALPH_PROMPT" ]]; then
        error "RALPH.md not found at: $RALPH_PROMPT"
        exit 1
    fi

    if [[ ! -f "$SCRIPT_DIR/spec/DESIGN.md" ]]; then
        error "spec/DESIGN.md not found at: $SCRIPT_DIR/spec/DESIGN.md"
        exit 1
    fi

    if [[ ! -f "$SCRIPT_DIR/spec/TASKS.md" ]]; then
        error "spec/TASKS.md not found at: $SCRIPT_DIR/spec/TASKS.md"
        exit 1
    fi

    success "Prerequisites check passed"
}

run_iteration() {
    local iteration=$1
    local log_file="$LOG_DIR/ralph_${TIMESTAMP}_iter${iteration}.log"

    log "Starting iteration $iteration..."
    log "Log file: $log_file"

    if [[ "$DRY_RUN" == "true" ]]; then
        log "[DRY RUN] Would execute:"
        echo "  cd $SCRIPT_DIR"
        echo "  claude --dangerously-skip-permissions -p \"\$(cat $RALPH_PROMPT)\""
        return 0
    fi

    cd "$SCRIPT_DIR"

    local exit_code=0

    if [[ "$VERBOSE" == "true" ]]; then
        log "Running... (verbose mode)"
        if claude --dangerously-skip-permissions \
                  --output-format stream-json \
                  --verbose \
                  -p "$(cat "$RALPH_PROMPT")" 2>&1 | tee "$log_file"; then
            exit_code=0
        else
            exit_code=$?
        fi
    else
        log "Running..."
        if claude --dangerously-skip-permissions \
                  -p "$(cat "$RALPH_PROMPT")" > "$log_file" 2>&1; then
            exit_code=0
        else
            exit_code=$?
        fi
    fi

    echo ""
    echo "┌─────────────────────────────────────────────────────────────────┐"
    printf  "│                   ITERATION %-3s SUMMARY                         │\n" "$iteration"
    echo "└─────────────────────────────────────────────────────────────────┘"
    echo ""
    tail -20 "$log_file"
    echo ""

    if [[ $exit_code -eq 0 ]]; then
        success "Iteration $iteration completed successfully"
        return 0
    else
        error "Iteration $iteration failed (exit code: $exit_code)"
        return 1
    fi
}

main() {
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║           RALPH - Autonomous Development Loop                 ║"
    echo "║                     petermark.dev                             ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""

    check_prerequisites

    if [[ "$SINGLE_RUN" == "true" ]]; then
        log "Running single iteration..."
        scan_for_secrets
        run_iteration 1
        exit $?
    fi

    log "Starting autonomous loop (max $MAX_ITERATIONS iterations)..."
    log "Press Ctrl+C to stop"
    echo ""

    for ((i=1; i<=MAX_ITERATIONS; i++)); do
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        log "ITERATION $i of $MAX_ITERATIONS"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

        scan_for_secrets

        if run_iteration "$i"; then
            success "Iteration $i complete"
        else
            warn "Iteration $i had issues, continuing..."
        fi

        if [[ $i -lt $MAX_ITERATIONS ]]; then
            log "Waiting $ITERATION_DELAY seconds before next iteration..."
            sleep $ITERATION_DELAY
        fi
    done

    warn "Reached maximum iterations ($MAX_ITERATIONS)"
}

trap 'echo ""; warn "Interrupted by user"; exit 130' INT

main "$@"
