# Accessing HolyPearl WordPress admin

**Site:** https://holypearl.co.il  
**Hosting:** WordPress.com Business (login often via WordPress.com)

## For you (human login)

1. Open **https://holypearl.co.il/wp-admin/**  
2. Or use **Log in with WordPress.com** on https://holypearl.co.il/wp-login.php  
3. After login: **Pages →** find draft page **3702** (do not edit page **52**)

## For the Cloud Agent (automated deploy)

This environment has **no WordPress credentials** unless you add them as **Cursor Secrets** for the project:

| Secret name | Value |
|-------------|--------|
| `HP_WP_USER` | WordPress username (or email) |
| `HP_WP_APP_PASSWORD` | [Application Password](https://wordpress.com/support/security/application-passwords/) — spaces optional |

Create Application Password:

1. Log in to wp-admin  
2. **Users → Profile** (or your user)  
3. **Application Passwords** → name e.g. `Cursor Agent` → **Add**  
4. Copy the generated password once  

Then ask the agent to run:

```bash
./scripts/deploy-hp3702-plugin.sh
```

Or to verify API access:

```bash
curl -s -u "$HP_WP_USER:$HP_WP_APP_PASSWORD" \
  "https://holypearl.co.il/wp-json/wp/v2/users/me" | python3 -m json.tool
```

## Manual homepage update (no API)

1. **Plugins → Add New → Upload** → `wordpress/dist/holypearl-hp3702-draft.zip` → **Activate**  
2. Preview page **3702** (stay **Draft**)

## Security

- Never commit passwords to this repo  
- Revoke Application Passwords when done  
- Agent cannot complete CAPTCHA on wp-login.php — API password is required  
