# Frontier 150 — OpenAI API Integration Note

An encrypted OpenAI Platform API-key setup flow was opened for this research project. The raw key is not returned to chat and must not be committed to GitHub.

For Supabase Edge Functions, store the key as a production secret/environment variable (for example `OPENAI_API_KEY`) and read it with `Deno.env.get('OPENAI_API_KEY')`. Never log the key or place it in client-side code. Local `.env` files must remain untracked.

This repository contains only this handling note; it intentionally contains no credential value.
