# ensure: npm install -g @cloudflare/wrangler
npx wrangler login
npx wrangler pages deploy ./ --project-name={{PROJECT_NAME}} --commit-dirty=true