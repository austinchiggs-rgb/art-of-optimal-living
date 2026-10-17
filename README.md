# The Art of Optimal Living

Static website for `artofoptimalliving.com`.

## Local preview

Run from the project directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8000/`.

## Deployment

The repository has no build step. Deploy the repository root to any static host. The included `_headers` file configures security and cache headers on hosts that support the Netlify/Cloudflare Pages headers format. Configure the custom domain `artofoptimalliving.com`, redirect the alternate `www` hostname to the canonical hostname, and enforce HTTPS in the hosting provider.

Before production launch:

1. Replace the placeholder mailing-list form action and bot-field name in `index.html` with values from the selected email provider.
2. Configure that provider to deliver the completed guide after signup.
3. Confirm the deployed URLs in `sitemap.xml` and submit it to the appropriate search-engine webmaster tools.
4. Test the homepage, legal pages, 404 handling, outbound links, and email signup on the production domain.
