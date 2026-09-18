#!/usr/bin/env bash
# Verifica (y despierta si hace falta) la app de Streamlit. Responde VIVA o DORMIDA.
# Uso:  .github/scripts/verificar.sh
set -euo pipefail
cd "$(dirname "$0")"
if [ ! -d node_modules/playwright-core ] && [ ! -d node_modules/playwright ]; then
  echo "instalando playwright-core (solo la primera vez)..." >&2
  npm install --silent --no-save --no-audit --no-fund playwright-core >&2
fi
export CHROME_PATH="${CHROME_PATH:-$(command -v google-chrome-stable || command -v chromium || true)}"
export APP_URL="${APP_URL:-https://resultados-icfes-pcielo-2025.streamlit.app/}"
exec node keep-alive.mjs
