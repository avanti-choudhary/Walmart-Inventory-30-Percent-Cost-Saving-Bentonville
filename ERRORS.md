# ERRORS.md - Project 3: Walmart 30% Inventory Cost Reduction (Bentonville)

This file logs every real error we hit while building, uploading, and publishing this repo. Each error includes fix.

## 1. GitHub Publishing Errors

### Error 1: Could not find About section
**Problem:** Looked for About section on profile page `github.com/avanti-choudhary` but it doesn't exist there.
**Solution:** About section is ONLY inside the repo page: `github.com/avanti-choudhary/Walmart-Inventory-30-Percent-Cost-Saving-Bentonville` -> right side -> gear icon.

### Error 2: Topics rejected - "Bentonville" with capital B
**Problem:** Tried to add topic `Bentonville` with capital B, GitHub would not accept.
**Solution:** GitHub topics must be all lowercase. Use `bentonville` not `Bentonville`.

### Error 3: Topics typed but not saved
**Problem:** Typed `bentonville` in Topics box but it stayed grey and didn't add.
**Solution:** Must press **Enter** after typing each topic to turn it into a blue pill with `x`. Then click Save changes.

### Error 4: Description missing after repo creation
**Problem:** After uploading, About showed "No description, website, or topics provided."
**Solution:** Click gear ⚙️ icon in About -> Add Description: `Bentonville AR project: Cut slow-moving inventory 30% using SQL LAG() + Python. Saved $27,720 (13.96% total cost). Includes dashboard + ERRORS.md`

### Error 5: Confusion between Profile Pin vs Repo page
**Problem:** Tried to customize pins but clicked on profile customization instead of repo details.
**Solution:** To pin: Profile page -> Customize your pins -> Check the Walmart repo box -> Save. To edit description: Repo page -> About gear icon.

### Error 6: Deployment / Website field confusion
**Problem:** In Edit repository details popup, confused about Website, Deployments, Releases, Packages checkboxes.
**Solution:** Leave Website blank (optional). Keep Releases checked. Deployments unchecked is fine for this data project.

## 2. Project Data Errors (Original Analysis)

### Error 7: Slow-moving inventory miscalculation
**Problem:** Initial SQL query without LAG() window function flagged fast-moving items as slow.
**Solution:** Used SQL `LAG(stock_level) OVER (PARTITION BY product_id ORDER BY date)` to track trend and correctly identify 30% slow-moving.

### Error 8: Cost saving total mismatch
**Problem:** Excel sum showed different total than Python pandas sum.
**Solution:** Found duplicate rows in Data folder CSV. Removed duplicates with `df.drop_duplicates()` before calculating $27,720 saved (13.96% reduction).

### Error 9: Dashboard not showing in GitHub
**Problem:** Uploaded Dashboard folder but images didn't render in README.
**Solution:** Used relative path `./Dashboard/dashboard.png` instead of absolute path in README.md.

## Final Result - All Solved ✅
- Repo is public: `Walmart-Inventory-30-Percent-Cost-Saving-Bentonville`
- Description added with $27,720 saving
- 5 topics added: walmart, inventory-optimization, sql, python, bentonville
- Pinned to profile: github.com/avanti-choudhary
- All files visible: Dashboard/, Data/, ERRORS.md, README.md