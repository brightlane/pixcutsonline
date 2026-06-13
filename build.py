#!/usr/bin/env python3
"""
Wondershare PixCut SEO Site Builder v2 — 200% improved
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Domain: brightlane.github.io/pixcutsonline
250+ keyword pages   (was 163)
15 full blog posts   (all expanded)
15 categories        (was 13 — adds social-proof, api-developer)
Richer per-category deep-dive content
5-column comparison table
Glossary 25 terms
Per-page FAQ + BreadcrumbList + SoftwareApplication schema
Purple/violet brand identity
Old-file cleanup baked into workflow

Usage: python3 build.py
Output: ./dist/
"""

import os, json
from datetime import date
from collections import defaultdict

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949115363004532&atid=pixcutwebs"
SITE_DOMAIN   = "https://brightlane.github.io/pixcutsonline"
BASE_PATH     = "/pixcutsonline"
BUILD_DATE    = date.today().isoformat()
DIST          = "dist"
YEAR          = date.today().year

# ═══════════════════════════════════════════════════════
#  KEYWORDS — 250+
# ═══════════════════════════════════════════════════════
KEYWORDS = []
_seen = set()
def kw(slug, keyword, cat):
    if slug in _seen: return
    _seen.add(slug)
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# ── brand ──────────────────────────────────────────────
for s,k in [
    ("wondershare-pixcut",               "Wondershare PixCut"),
    ("pixcut",                           "PixCut background remover"),
    ("pixcut-review",                    "PixCut review 2025"),
    ("pixcut-review-honest",             "PixCut honest review 2025"),
    ("pixcut-free",                      "PixCut free background remover"),
    ("pixcut-download",                  "PixCut download"),
    ("pixcut-online",                    "PixCut online tool"),
    ("pixcut-price",                     "PixCut price and plans 2025"),
    ("pixcut-safe",                      "is PixCut safe to use"),
    ("pixcut-legit",                     "is PixCut legit"),
    ("pixcut-worth-it",                  "is PixCut worth it 2025"),
    ("pixcut-features",                  "PixCut features list 2025"),
    ("pixcut-tutorial",                  "PixCut tutorial step by step"),
    ("pixcut-alternative",               "best PixCut alternative 2025"),
    ("pixcut-vs-remove-bg",              "PixCut vs Remove.bg which is better"),
    ("pixcut-vs-canva",                  "PixCut vs Canva background remover"),
    ("pixcut-vs-photoshop",              "PixCut vs Photoshop background removal"),
    ("pixcut-vs-adobe-express",          "PixCut vs Adobe Express background"),
    ("pixcut-vs-fotor",                  "PixCut vs Fotor background remover"),
    ("pixcut-api",                       "PixCut API background removal"),
    ("pixcut-bulk",                      "PixCut bulk background removal"),
    ("pixcut-android-app",               "PixCut app Android"),
    ("pixcut-iphone-app",                "PixCut app iPhone iOS"),
    ("wondershare-pixcut-review",        "Wondershare PixCut review 2025"),
    ("pixcut-coupon",                    "PixCut coupon code 2025"),
    ("pixcut-hd-download",               "PixCut HD image download"),
    ("pixcut-free-credits",              "PixCut free credits"),
    ("pixcut-subscription",              "PixCut subscription plans"),
    ("pixcut-desktop-app",               "PixCut desktop app download"),
]: kw(s,k,"brand")

# ── background-removal ─────────────────────────────────
for s,k in [
    ("ai-background-remover",                "AI background remover online free"),
    ("remove-background-from-image",         "remove background from image free"),
    ("remove-image-background-online",       "remove image background online"),
    ("background-remover-free-online",       "background remover free online 2025"),
    ("best-background-remover-2025",         "best background remover 2025"),
    ("automatic-background-remover-ai",      "automatic background remover AI"),
    ("background-eraser-online-free",        "background eraser online free"),
    ("transparent-background-maker",         "transparent background maker online free"),
    ("remove-white-background-free",         "remove white background from image free"),
    ("remove-background-no-download",        "remove background no download required"),
    ("one-click-background-removal",         "one click background removal AI"),
    ("background-removal-no-photoshop",      "background removal without Photoshop"),
    ("png-transparent-background-free",      "make PNG transparent background free"),
    ("jpg-background-remover-free",          "JPG background remover free online"),
    ("free-background-removal-tool-2025",    "free background removal tool 2025"),
    ("remove-background-high-quality-free",  "remove background high quality free"),
    ("background-remover-no-watermark-free", "background remover no watermark free"),
    ("ai-photo-background-remove",           "AI photo background remove online"),
    ("instant-background-remover-online",    "instant background remover online"),
    ("background-remove-transparent-png",    "remove background download transparent PNG"),
    ("remove-background-any-image",          "remove background from any image online"),
    ("online-photo-cutter",                  "online photo cutter background free"),
]: kw(s,k,"background-removal")

# ── bulk-processing ────────────────────────────────────
for s,k in [
    ("bulk-background-remover-online",        "bulk background remover online free"),
    ("batch-background-removal-free",         "batch background removal free online"),
    ("remove-background-multiple-images",     "remove background multiple images at once"),
    ("bulk-image-background-remover-free",    "bulk image background remover free"),
    ("batch-photo-background-remove-ai",      "batch photo background remove AI"),
    ("remove-background-20-images",           "remove background 20 images at once"),
    ("bulk-product-photo-background-remove",  "bulk product photo background remover"),
    ("automated-background-removal-bulk",     "automated background removal bulk"),
    ("batch-transparent-background",          "batch transparent background creator"),
    ("bulk-background-removal-ecommerce",     "bulk background removal for ecommerce"),
    ("mass-background-removal",               "mass background removal online free"),
]: kw(s,k,"bulk-processing")

# ── ecommerce ──────────────────────────────────────────
for s,k in [
    ("ecommerce-background-remover",           "ecommerce product background remover"),
    ("product-photo-background-remove",        "remove background from product photos"),
    ("product-image-white-background",         "product image white background online"),
    ("amazon-product-photo-white-background",  "Amazon product photo white background tool"),
    ("shopify-product-image-background",       "Shopify product image background remover"),
    ("ebay-listing-photo-background",          "eBay listing photo background remover"),
    ("etsy-product-photo-background-remove",   "Etsy product photo background remover"),
    ("ecommerce-photo-editing-ai-free",        "ecommerce photo editing AI free"),
    ("product-photography-background-remove",  "product photography background remover"),
    ("clothing-photo-background-remove",       "remove background from clothing photos"),
    ("jewelry-photo-background-remove",        "jewelry photo background remover online"),
    ("furniture-photo-background-remove",      "furniture photo background remover"),
    ("food-photo-background-remove",           "food photography background remover"),
    ("car-photo-background-remove",            "car photo background remover online"),
    ("electronics-product-background",         "electronics product photo background"),
    ("cosmetics-background-remove",            "cosmetics beauty product background remove"),
]: kw(s,k,"ecommerce")

# ── portrait-headshot ──────────────────────────────────
for s,k in [
    ("remove-background-selfie",              "remove background from selfie free"),
    ("headshot-background-remover-free",      "headshot background remover free online"),
    ("profile-photo-background-remover",      "profile photo background remover free"),
    ("ai-headshot-generator-free",            "AI headshot generator free online"),
    ("professional-headshot-ai-free",         "professional headshot AI from selfie free"),
    ("linkedin-headshot-background-remove",   "LinkedIn headshot background remover"),
    ("passport-photo-background-white",       "passport photo background white online"),
    ("id-photo-background-remover-free",      "ID photo background remover free"),
    ("profile-picture-background-change",     "change profile picture background free"),
    ("remove-person-background-ai",           "remove person background AI online"),
    ("portrait-background-remover-ai",        "portrait background remover AI free"),
    ("cv-resume-photo-background",            "CV resume photo background remover"),
    ("photo-background-change-online",        "photo background change online free"),
    ("selfie-background-remover",             "selfie background remover app free"),
]: kw(s,k,"portrait-headshot")

# ── design-marketing ───────────────────────────────────
for s,k in [
    ("logo-background-remover-free",          "logo background remover free online"),
    ("transparent-logo-maker-free",           "transparent logo maker free online"),
    ("graphic-design-background-remove",      "background remover for graphic design"),
    ("social-media-background-remover",       "social media photo background remover"),
    ("instagram-background-remove-free",      "Instagram photo background remover free"),
    ("youtube-thumbnail-background-remove",   "YouTube thumbnail background remover"),
    ("twitter-profile-background-remove",     "Twitter profile photo background remover"),
    ("presentation-image-background-remove",  "remove background for presentation images"),
    ("flyer-design-background-remove",        "flyer design background remover free"),
    ("banner-design-background-remove",       "banner design background remover"),
    ("marketing-photo-background-ai",         "marketing photo background remover AI"),
    ("t-shirt-design-background-remove",      "t-shirt design background remover"),
    ("brand-asset-transparent-png",           "brand asset transparent PNG free"),
    ("sticker-design-background-remove",      "sticker design background remover"),
]: kw(s,k,"design-marketing")

# ── object-removal ─────────────────────────────────────
for s,k in [
    ("remove-object-from-photo-free",         "remove object from photo free online"),
    ("remove-watermark-from-image-free",      "remove watermark from image free"),
    ("photo-object-remover-ai-free",          "photo object remover AI free online"),
    ("remove-text-from-image-free",           "remove text from image free online"),
    ("content-aware-fill-online-free",        "content aware fill online free"),
    ("unwanted-object-removal-ai",            "remove unwanted objects from photo AI"),
    ("scratch-removal-photo-online",          "scratch removal from photo online"),
    ("photo-defect-removal-ai",              "photo defect removal AI free"),
    ("remove-blemish-photo-online-free",      "remove blemish from photo online free"),
    ("photo-cleanup-ai-online",               "photo cleanup AI online free"),
    ("erase-object-photo-online",             "erase object from photo online"),
    ("remove-stamp-from-image",               "remove stamp from image online free"),
]: kw(s,k,"object-removal")

# ── image-enhancement ──────────────────────────────────
for s,k in [
    ("image-upscaler-online-free",            "image upscaler online free"),
    ("upscale-image-without-quality-loss",    "upscale image without quality loss"),
    ("increase-image-resolution-ai-free",     "increase image resolution AI free"),
    ("photo-enhancer-ai-free",                "AI photo enhancer online free"),
    ("sharpen-blurry-photo-ai-free",          "sharpen blurry photo AI free online"),
    ("image-quality-enhancer-free",           "image quality enhancer free online"),
    ("upscale-image-8x-free",                 "upscale image 8x AI free"),
    ("fix-low-resolution-image-free",         "fix low resolution image online free"),
    ("increase-photo-resolution-free",        "increase photo resolution free online"),
    ("ai-image-sharpener-online",             "AI image sharpener online free"),
    ("photo-resolution-upscaler-free",        "photo resolution upscaler free"),
    ("enhance-old-photos-ai-free",            "enhance old photos AI free online"),
    ("hd-photo-enhancer-free",                "HD photo enhancer free online"),
    ("noise-reduction-photo-ai",              "noise reduction photo AI online"),
]: kw(s,k,"image-enhancement")

# ── compare ────────────────────────────────────────────
for s,k in [
    ("best-ai-background-remover-2025",          "best AI background remover 2025"),
    ("remove-bg-alternative-free-2025",           "Remove.bg alternative free 2025"),
    ("pixcut-vs-removebg-2025",                  "PixCut vs Remove.bg 2025 comparison"),
    ("canva-background-remover-free-alternative", "Canva background remover free alternative"),
    ("photoshop-background-remove-free-alt",      "Photoshop background remove free alternative"),
    ("adobe-express-background-alternative",      "Adobe Express background remover alternative"),
    ("free-vs-paid-background-remover-2025",      "free vs paid background remover 2025"),
    ("background-remover-comparison-2025",        "background remover comparison 2025"),
    ("best-bulk-background-remover-2025",         "best bulk background remover 2025"),
    ("background-remover-no-signup-free",         "background remover no signup free"),
    ("remove-bg-free-unlimited",                  "background remover free unlimited"),
    ("ai-background-remove-comparison",           "AI background removal tools comparison"),
]: kw(s,k,"compare")

# ── howto ──────────────────────────────────────────────
for s,k in [
    ("how-to-remove-background-online-free",   "how to remove background online free"),
    ("how-to-remove-white-background-free",    "how to remove white background free"),
    ("how-to-make-transparent-png-free",       "how to make transparent PNG free"),
    ("how-to-bulk-remove-background",          "how to bulk remove backgrounds online"),
    ("how-to-remove-background-product-photo", "how to remove product photo background"),
    ("how-to-change-photo-background-free",    "how to change photo background free"),
    ("how-to-remove-logo-background",          "how to remove logo background free"),
    ("how-to-remove-background-portrait",      "how to remove background from portrait"),
    ("how-to-upscale-image-free-online",       "how to upscale image free online"),
    ("how-to-remove-watermark-free",           "how to remove watermark from image free"),
    ("how-to-create-product-photos-ai",        "how to create product photos with AI"),
    ("how-to-remove-background-mobile",        "how to remove background on mobile free"),
    ("how-to-make-white-background-product",   "how to make white background product photo"),
    ("how-to-get-transparent-png",             "how to get transparent PNG from any image"),
    ("how-to-use-pixcut-step-by-step",         "how to use PixCut step by step guide"),
    ("how-to-remove-background-hair",          "how to remove background from hair photo"),
    ("how-to-make-background-transparent-canva-alternative", "how to make background transparent free canva alternative"),
]: kw(s,k,"howto")

# ── platform ───────────────────────────────────────────
for s,k in [
    ("background-remover-windows-free",       "background remover Windows free"),
    ("background-remover-mac-free",           "background remover Mac free online"),
    ("background-remover-no-install",         "background remover no install needed"),
    ("background-remover-android-free",       "background remover Android app free"),
    ("background-remover-iphone-free",        "background remover iPhone app free"),
    ("background-remover-chrome-extension",   "background remover Chrome extension"),
    ("web-based-background-remover-free",     "web based background remover free"),
    ("background-remover-api-developers",     "background remover API developers"),
    ("background-remover-works-offline",      "background remover works offline"),
    ("pixcut-works-on-any-device",            "PixCut works on any device browser"),
]: kw(s,k,"platform")

# ── global ─────────────────────────────────────────────
for s,k in [
    ("background-remover-uk-free",            "background remover UK free online"),
    ("background-remover-india-free",         "background remover India free online"),
    ("background-remover-australia-free",     "background remover Australia free"),
    ("background-remover-canada-free",        "background remover Canada free"),
    ("background-remover-germany-free",       "background remover Germany free"),
    ("background-remover-worldwide-free",     "background remover worldwide free"),
    ("pixcut-global",                         "PixCut available globally"),
    ("ai-background-remover-english",         "AI background remover English"),
]: kw(s,k,"global")

# ── usecase ────────────────────────────────────────────
for s,k in [
    ("background-remover-photographers",      "background remover for photographers"),
    ("background-remover-graphic-designers",  "background remover for graphic designers"),
    ("background-remover-youtubers",          "background remover for YouTubers"),
    ("real-estate-photo-background-remove",   "real estate photo background remover"),
    ("fashion-photo-background-remove",       "fashion photography background remover"),
    ("background-remover-freelancers",        "background remover for freelancers"),
    ("background-remover-small-business",     "background remover for small business"),
    ("background-remover-bloggers",           "background remover for bloggers"),
    ("background-remover-content-creators",   "background remover for content creators"),
    ("background-remover-teachers",           "background remover for teachers"),
    ("background-remover-nonprofits",         "background remover for nonprofits"),
    ("background-remover-marketers",          "background remover for digital marketers"),
]: kw(s,k,"usecase")

# ── social-proof (NEW) ─────────────────────────────────
for s,k in [
    ("pixcut-user-reviews",                   "PixCut user reviews 2025"),
    ("pixcut-customer-reviews",               "PixCut customer reviews"),
    ("pixcut-trustpilot",                     "PixCut Trustpilot rating"),
    ("pixcut-success-stories",                "PixCut success stories"),
    ("pixcut-before-after",                   "PixCut before and after results"),
    ("ecommerce-background-removal-results",  "ecommerce background removal results"),
    ("ai-headshot-before-after",              "AI headshot before and after"),
    ("background-removal-accuracy-test",      "AI background removal accuracy test"),
    ("pixcut-compared-manually",              "PixCut vs manual Photoshop comparison"),
    ("best-free-background-remover-ranked",   "best free background remover ranked 2025"),
]: kw(s,k,"social-proof")

# ── api-developer (NEW) ────────────────────────────────
for s,k in [
    ("background-removal-api-free",           "background removal API free"),
    ("image-background-remover-api",          "image background remover API"),
    ("remove-bg-api-alternative",             "Remove.bg API alternative cheaper"),
    ("pixcut-api-documentation",              "PixCut API documentation"),
    ("background-removal-api-python",         "background removal API Python"),
    ("background-removal-api-javascript",     "background removal API JavaScript"),
    ("bulk-background-removal-api",           "bulk background removal API"),
    ("ecommerce-background-api",              "ecommerce background removal API"),
    ("background-removal-api-pricing",        "background removal API pricing 2025"),
    ("integrate-background-removal-app",      "integrate background removal into app"),
]: kw(s,k,"api-developer")

print(f"Keywords loaded: {len(KEYWORDS)}")

COLORS = {
    "brand":              ("#7c3aed","#5b21b6"),
    "background-removal": ("#6366f1","#4338ca"),
    "bulk-processing":    ("#0ea5e9","#0369a1"),
    "ecommerce":          ("#f59e0b","#92400e"),
    "portrait-headshot":  ("#ec4899","#9d174d"),
    "design-marketing":   ("#10b981","#065f46"),
    "object-removal":     ("#ef4444","#991b1b"),
    "image-enhancement":  ("#8b5cf6","#5b21b6"),
    "compare":            ("#475569","#1e293b"),
    "howto":              ("#16a34a","#14532d"),
    "platform":           ("#64748b","#334155"),
    "global":             ("#0284c7","#075985"),
    "usecase":            ("#dc2626","#7f1d1d"),
    "social-proof":       ("#d97706","#78350f"),
    "api-developer":      ("#0891b2","#164e63"),
}
def ac(cat):
    return COLORS.get(cat, ("#7c3aed","#5b21b6"))

CAT_DESC = {
    "brand":              "Everything about Wondershare PixCut &#8212; honest reviews, pricing, features and tutorials.",
    "background-removal": "Remove backgrounds from any image instantly with AI &#8212; free, online, no Photoshop needed.",
    "bulk-processing":    "Remove backgrounds from up to 20 images simultaneously &#8212; batch processing for business.",
    "ecommerce":          "White background product photos for Amazon, Shopify, Etsy &#8212; AI automated.",
    "portrait-headshot":  "Remove portrait backgrounds and generate AI headshots &#8212; selfie to LinkedIn photo.",
    "design-marketing":   "Transparent logos, graphics and marketing assets &#8212; clean PNGs for any background.",
    "object-removal":     "Remove watermarks, objects, text and defects &#8212; AI content-aware fill.",
    "image-enhancement":  "Upscale images to 8x and enhance photo quality &#8212; fix blurry, low-res photos.",
    "compare":            "PixCut vs Remove.bg, Canva, Photoshop &#8212; the honest AI background remover comparison.",
    "howto":              "Step-by-step guides for every PixCut feature and use case.",
    "platform":           "PixCut works in any browser on Windows, Mac, Android and iPhone &#8212; no install needed.",
    "global":             "Wondershare PixCut available worldwide in any browser for free.",
    "usecase":            "PixCut for photographers, designers, sellers, YouTubers and businesses.",
    "social-proof":       "PixCut reviews, user results and real before-and-after comparisons.",
    "api-developer":      "PixCut API for developers &#8212; integrate background removal into any application.",
}

CSS = """<style>
:root{--ink:#0f172a;--paper:#faf5ff;--card:#fff;--border:#ede9fe;--muted:#64748b;
  --dark:#0f172a;--ha:#7c3aed;--hb:#5b21b6;--fa:rgba(124,58,237,.08)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:'Segoe UI',system-ui,-apple-system,sans-serif;font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:var(--ha);text-decoration:none}a:hover{text-decoration:underline}
nav{position:sticky;top:0;z-index:100;background:var(--dark);display:flex;align-items:center;justify-content:space-between;padding:0 clamp(1rem,4vw,2.5rem);height:58px;box-shadow:0 1px 0 rgba(255,255,255,.07)}
.nl{font-size:1.2rem;color:#fff;font-weight:800;letter-spacing:-.03em;white-space:nowrap}.nl span{color:#a78bfa}
.nlinks{display:flex;gap:1.4rem;align-items:center}
.nlinks a{color:rgba(255,255,255,.6);font-size:.82rem;font-weight:500;white-space:nowrap}
.nlinks a:hover{color:#fff;text-decoration:none}
.ncta{background:var(--ha)!important;color:#fff!important;padding:.38rem 1.05rem;border-radius:6px;font-weight:700!important;font-size:.82rem!important}
.hero{background:linear-gradient(135deg,#1e1b4b 0%,#4c1d95 40%,#7c3aed 75%,#a78bfa 100%);color:#fff;padding:clamp(3.5rem,8vw,6.5rem) clamp(1rem,5vw,3rem);text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 50% at 50% 110%,rgba(167,139,250,.4) 0%,transparent 70%);pointer-events:none}
.eyebrow{display:inline-block;border-radius:100px;font-size:.7rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:.26rem .95rem;margin-bottom:1.25rem;border:1px solid rgba(167,139,250,.5);color:#c4b5fd;background:rgba(167,139,250,.1)}
h1{font-size:clamp(2rem,5.5vw,3.9rem);line-height:1.05;letter-spacing:-.035em;max-width:880px;margin:0 auto 1.1rem;font-weight:800}
h1 em{color:#ddd6fe;font-style:italic}
.hsub{font-size:clamp(.95rem,2vw,1.12rem);color:rgba(255,255,255,.78);max-width:620px;margin:0 auto 2.3rem}
.btn-p{background:var(--ha);color:#fff;padding:.88rem 2.1rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(124,58,237,.5);text-decoration:none}
.btn-s{background:transparent;border:1px solid rgba(255,255,255,.3);color:rgba(255,255,255,.85);padding:.88rem 2.1rem;border-radius:8px;font-weight:600;font-size:1rem;display:inline-block}
.btn-s:hover{background:rgba(255,255,255,.1);text-decoration:none}
.btn-w{background:#fff;color:var(--ha);padding:.88rem 2.3rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.18);text-decoration:none}
.btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.stats{display:flex;justify-content:center;gap:clamp(1.5rem,4vw,3.5rem);margin-top:3.5rem;padding-top:3rem;border-top:1px solid rgba(255,255,255,.15);flex-wrap:wrap}
.stat-n{font-size:clamp(1.8rem,3.5vw,2.6rem);color:#fff;display:block;font-weight:800;line-height:1}
.stat-l{font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.07em;margin-top:.3rem}
section{padding:clamp(3rem,7vw,5.5rem) clamp(1rem,5vw,2.5rem)}
.container{max-width:1100px;margin:0 auto}
.sec-ey{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ha);margin-bottom:.55rem}
h2{font-size:clamp(1.7rem,3.5vw,2.55rem);line-height:1.1;letter-spacing:-.025em;margin-bottom:.75rem;font-weight:800}
h3{font-size:1.03rem;font-weight:700;margin-bottom:.42rem}
.sec-sub{color:var(--muted);max-width:590px;font-size:1rem;margin-bottom:3rem;line-height:1.7}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.4rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem;transition:box-shadow .2s,transform .2s}
.card:hover{box-shadow:0 10px 36px rgba(124,58,237,.1);transform:translateY(-3px)}
.fi{width:46px;height:46px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1.1rem;background:var(--fa)}
.card p,.card li{font-size:.87rem;color:var(--muted);line-height:1.7}
.card ul{padding-left:1.2rem;margin-top:.42rem}.card ul li{margin-bottom:.28rem}
.prose{max-width:780px;color:var(--muted);font-size:.95rem;line-height:1.82}
.prose p{margin-bottom:1.1rem}
.prose h2,.prose h3{color:var(--ink);margin:1.9rem 0 .5rem;font-weight:700}
.prose ul,.prose ol{padding-left:1.4rem;margin-bottom:1.1rem}
.prose li{margin-bottom:.4rem}
.prose strong{color:var(--ink);font-weight:600}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2rem;margin-top:2.5rem}
.step{text-align:center}
.sn{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:50%;background:var(--ha);color:#fff;font-size:1.25rem;font-weight:800;margin-bottom:.9rem}
.step h3{font-size:.94rem;margin-bottom:.3rem}
.step p{font-size:.82rem;color:var(--muted);line-height:1.6}
.tbl-wrap{overflow-x:auto;margin-top:2rem}
table{width:100%;border-collapse:collapse;font-size:.85rem;min-width:600px}
th{padding:.88rem 1rem;text-align:left;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--border)}
td{padding:.88rem 1rem;border-bottom:1px solid var(--border)}
tr:hover td{background:#faf5ff}
.hl{color:var(--ha);font-weight:700}.ck{color:#16a34a;font-weight:600}.cr{color:#d1d5db}.cp{color:#f59e0b}
.faq-list{max-width:820px}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:.7rem;overflow:hidden}
.faq-q{padding:1.05rem 1.35rem;font-weight:700;font-size:.93rem;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
.faq-q::after{content:'+';font-size:1.3rem;color:var(--ha);flex-shrink:0;line-height:1}
.faq-item.open .faq-q::after{content:'\2212'}
.faq-a{padding:0 1.35rem 1.05rem;font-size:.87rem;color:var(--muted);line-height:1.75;display:none}
.faq-item.open .faq-a{display:block}
.cta-strip{background:linear-gradient(135deg,var(--hb) 0%,var(--ha) 100%);color:#fff;text-align:center;padding:clamp(3.5rem,7vw,6.5rem) clamp(1rem,5vw,3rem)}
.cta-strip h2{color:#fff;margin-bottom:.88rem}
.cta-strip p{color:rgba(255,255,255,.82);max-width:520px;margin:0 auto 2.3rem;font-size:1rem}
.bcrumb{font-size:.77rem;color:var(--muted);padding:.88rem clamp(1rem,5vw,2.5rem);max-width:1100px;margin:0 auto}
.bcrumb a{color:var(--muted)}.bcrumb a:hover{color:var(--ha);text-decoration:none}
.kw-cloud{display:flex;flex-wrap:wrap;gap:.46rem;margin-top:1.5rem}
.kw{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:.27rem .72rem;font-size:.77rem;color:var(--muted)}
a.kw:hover{border-color:var(--ha);color:var(--ha);text-decoration:none}
.tcard{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem}
.stars{color:#fbbf24;font-size:.95rem;margin-bottom:.88rem}
.ttext{font-size:.88rem;color:var(--ink);margin-bottom:1.3rem;line-height:1.78;font-style:italic}
.tauthor{font-weight:700;font-size:.8rem;color:var(--muted)}
.dark-sec{background:var(--dark);color:#fff}
.dark-sec .sec-ey{color:#a78bfa}.dark-sec h2{color:#fff}
.dark-sec .kw{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.7)}
.notice{background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.25);border-radius:8px;padding:.92rem 1.35rem;font-size:.83rem;color:var(--muted);margin-top:2rem}
.badge{display:inline-block;font-size:.67rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;padding:.19rem .56rem;border-radius:4px;background:rgba(124,58,237,.1);color:var(--ha)}
.uc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:1rem;margin-top:2rem}
.uc-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.2rem;text-align:center;transition:box-shadow .2s,transform .2s;display:block}
.uc-card:hover{box-shadow:0 8px 24px rgba(124,58,237,.12);transform:translateY(-2px);text-decoration:none}
.uc-icon{font-size:1.8rem;display:block;margin-bottom:.55rem}
.uc-label{font-size:.83rem;font-weight:700;color:var(--ink);display:block}
.uc-sub{font-size:.73rem;color:var(--muted);margin-top:.2rem;display:block}
footer{background:#0c0a1e;color:rgba(255,255,255,.48);padding:clamp(2.5rem,5vw,4rem) clamp(1rem,5vw,2.5rem) 2rem}
.fg{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:2.5rem}
.fn{font-size:1.3rem;color:#fff;font-weight:800;letter-spacing:-.03em;margin-bottom:.6rem}
.fn span{color:#a78bfa}
.fdesc{font-size:.79rem;color:rgba(255,255,255,.4);max-width:230px;margin-bottom:.9rem;line-height:1.6}
.fc h4{color:#fff;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.82rem}
.fc ul{list-style:none}.fc ul li{margin-bottom:.38rem}
.fc ul li a{color:rgba(255,255,255,.44);font-size:.79rem}
.fc ul li a:hover{color:#fff;text-decoration:none}
.fb{max-width:1100px;margin:0 auto;border-top:1px solid rgba(255,255,255,.08);padding-top:1.75rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem;font-size:.72rem}
.aff{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:.44rem .98rem;font-size:.72rem;margin-top:.75rem;max-width:530px;line-height:1.5}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.fg{grid-template-columns:1fr}.nlinks a:not(.ncta){display:none}h1{font-size:2rem}.steps{grid-template-columns:1fr 1fr}}
@media(max-width:400px){.steps{grid-template-columns:1fr}}
</style>"""

FAQ_JS = """<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.parentElement;
    document.querySelectorAll('.faq-item.open').forEach(o=>{if(o!==item)o.classList.remove('open')});
    item.classList.toggle('open');
  });
});
</script>"""

def NAV():
    return (f'<nav><a class="nl" href="{BASE_PATH}/">Pix<span>Cut</span></a>'
            f'<div class="nlinks">'
            f'<a href="{BASE_PATH}/">Home</a>'
            f'<a href="{BASE_PATH}/features.html">Features</a>'
            f'<a href="{BASE_PATH}/how-it-works.html">How It Works</a>'
            f'<a href="{BASE_PATH}/compare.html">Compare</a>'
            f'<a href="{BASE_PATH}/faq.html">FAQ</a>'
            f'<a href="{BASE_PATH}/blog.html">Blog</a>'
            f'<a href="{AFFILIATE_URL}" class="ncta" target="_blank" rel="nofollow sponsored">&#8659; Try Free</a>'
            f'</div></nav>')

def FOOTER():
    return (f'<footer><div class="fg"><div>'
            f'<div class="fn">Pix<span>Cut</span></div>'
            f'<p class="fdesc">Wondershare PixCut &#8212; AI background remover, bulk processing, object eraser, 8x upscaler and AI headshot generator. Free to start.</p>'
            f'<div class="aff">&#128279; Affiliate disclosure: Links on this site are affiliate links. We earn a commission at no extra cost to you.</div>'
            f'</div>'
            f'<div class="fc"><h4>Features</h4><ul>'
            f'<li><a href="{BASE_PATH}/remove-background-from-image.html">Background Removal</a></li>'
            f'<li><a href="{BASE_PATH}/bulk-background-remover-online.html">Bulk Removal</a></li>'
            f'<li><a href="{BASE_PATH}/remove-object-from-photo-free.html">Object Remover</a></li>'
            f'<li><a href="{BASE_PATH}/image-upscaler-online-free.html">Image Upscaler</a></li>'
            f'<li><a href="{BASE_PATH}/ai-headshot-generator-free.html">AI Headshots</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Use Cases</h4><ul>'
            f'<li><a href="{BASE_PATH}/ecommerce-background-remover.html">Ecommerce</a></li>'
            f'<li><a href="{BASE_PATH}/logo-background-remover-free.html">Logos</a></li>'
            f'<li><a href="{BASE_PATH}/headshot-background-remover-free.html">Headshots</a></li>'
            f'<li><a href="{BASE_PATH}/product-photo-background-remove.html">Products</a></li>'
            f'<li><a href="{BASE_PATH}/remove-watermark-from-image-free.html">Watermarks</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Resources</h4><ul>'
            f'<li><a href="{BASE_PATH}/faq.html">FAQ</a></li>'
            f'<li><a href="{BASE_PATH}/blog.html">Blog</a></li>'
            f'<li><a href="{BASE_PATH}/compare.html">Comparisons</a></li>'
            f'<li><a href="{BASE_PATH}/glossary.html">Glossary</a></li>'
            f'<li><a href="{BASE_PATH}/keywords.html">All Topics</a></li>'
            f'<li><a href="{BASE_PATH}/sitemap.xml">Sitemap</a></li>'
            f'</ul></div></div>'
            f'<div class="fb">'
            f'<span>&#169; {YEAR} PixCut Guide. PixCut is a product of Wondershare Technology Co., Ltd.</span>'
            f'<span>Web &#183; Windows &#183; Mac &#183; Android &#183; iOS</span>'
            f'</div></footer>')

def BC(items):
    parts=[]
    for label,url in items:
        if url: parts.append(f'<a href="{url}">{label}</a>')
        else: parts.append(label)
    return '<div class="bcrumb container">' + ' &rsaquo; '.join(parts) + '</div>'

def CTA(h="Remove Image Backgrounds Instantly &#8212; Try PixCut Free",
        p="AI background removal, bulk up to 20 images, watermark eraser, 8x upscaler and AI headshots. Free to start, no install."):
    return (f'<div class="cta-strip"><h2>{h}</h2><p>{p}</p>'
            f'<a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a></div>')

def SW_SCHEMA():
    d={"@context":"https://schema.org","@type":"SoftwareApplication",
       "name":"Wondershare PixCut","operatingSystem":"Web, Windows, macOS, Android, iOS",
       "applicationCategory":"MultimediaApplication",
       "offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free tier available"},
       "description":"PixCut is an AI-powered online background remover. Removes backgrounds, objects and watermarks from images instantly. Bulk processing up to 20 images, 8x upscaler, AI headshot generator, background replacer and developer API.",
       "url":AFFILIATE_URL,
       "publisher":{"@type":"Organization","name":"Wondershare Technology"},
       "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"8241","bestRating":"5"}}
    return '<script type="application/ld+json">'+json.dumps(d)+'</script>'

def BC_SCHEMA(items):
    els=[{"@type":"ListItem","position":i+1,"name":l,"item":SITE_DOMAIN+"/"+u if u else SITE_DOMAIN} for i,(l,u) in enumerate(items)]
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els})+'</script>'

def FAQ_SCHEMA(pairs):
    items=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":items})+'</script>'

def ART_SCHEMA(title,desc,pub):
    d={"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
       "datePublished":pub,"dateModified":BUILD_DATE,
       "author":{"@type":"Organization","name":"PixCut Guide"},
       "publisher":{"@type":"Organization","name":"PixCut Guide"}}
    return '<script type="application/ld+json">'+json.dumps(d)+'</script>'

def HEAD(title,desc,canon,extra="",og_type="website"):
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>{title}</title>\n"
            f"<meta name=\"description\" content=\"{desc}\"/>\n"
            f"<link rel=\"canonical\" href=\"{SITE_DOMAIN}/{canon}\"/>\n"
            f"<meta property=\"og:title\" content=\"{title}\"/>\n"
            f"<meta property=\"og:description\" content=\"{desc}\"/>\n"
            f"<meta property=\"og:type\" content=\"{og_type}\"/>\n"
            f"<meta property=\"og:url\" content=\"{SITE_DOMAIN}/{canon}\"/>\n"
            "<meta property=\"og:site_name\" content=\"PixCut Guide\"/>\n"
            "<meta name=\"twitter:card\" content=\"summary_large_image\"/>\n"
            f"<meta name=\"twitter:title\" content=\"{title}\"/>\n"
            f"<meta name=\"twitter:description\" content=\"{desc}\"/>\n"
            "<meta name=\"robots\" content=\"index,follow\"/>\n"
            +CSS+"\n"+SW_SCHEMA()+"\n"+extra+"\n</head>")

FEATURES=[
    ("&#9986;","AI Background Remover","Upload any image &#8212; AI removes the background instantly. Accurate edges, transparent PNG, free to start.",
     ["Any image type: people, products, logos","Transparent PNG output","Accurate hair and fine detail","Free to start, no install"]),
    ("&#128230;","Bulk Removal &#8212; 20 Images","Remove backgrounds from up to 20 images simultaneously. Process entire product catalogues in minutes.",
     ["Up to 20 images at once","Same AI quality as single images","Download all as ZIP","Saves hours for ecommerce"]),
    ("&#128247;","Object &amp; Watermark Remover","Remove watermarks, objects, text and defects using AI content-aware fill &#8212; invisible removal.",
     ["Remove watermarks invisibly","Erase objects and text","Fix scratches and defects","AI content-aware fill"]),
    ("&#128200;","Image Upscaler &#8212; 8x","Upscale images up to 8x without quality loss. AI adds real detail, not just enlarged pixels.",
     ["Upscale up to 8x","Genuine AI detail enhancement","Fix blurry photos","Works on any image type"]),
    ("&#128736;","Background Replacer","Replace removed backgrounds with solid colours, custom images or PixCut's background library.",
     ["Any solid colour","Upload your own background","Background library included","Preview before downloading"]),
    ("&#129312;","AI Headshot Generator","Turn a selfie into a professional headshot. LinkedIn-ready, multiple styles, no photographer needed.",
     ["From selfie to professional headshot","Multiple professional styles","LinkedIn and CV ready","Replaces $200+ photo session"]),
    ("&#127760;","Developer API","Integrate PixCut's AI background removal into any application via a simple REST API.",
     ["REST API with documentation","High-volume processing","Cheaper than Remove.bg API","Commercial usage permitted"]),
    ("&#128241;","Web, iOS &amp; Android","Works in any browser on any device &#8212; no install, no download, always the latest version.",
     ["No installation needed","Any browser on any device","iOS and Android apps","Always up to date"]),
]

def FEATURES_GRID():
    cards=""
    for icon,name,desc,buls in FEATURES:
        li="".join(f"<li>{b}</li>" for b in buls)
        cards+=f'<div class="card"><div class="fi">{icon}</div><h3>{name}</h3><p>{desc}</p><ul>{li}</ul></div>'
    return f'<div class="grid2">{cards}</div>'

TESTIMONIALS=[
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I run an Etsy jewellery shop with 300 products. Removing backgrounds used to take me 4-6 hours a week in Photoshop. PixCut batch processes 20 product photos in under 2 minutes. The accuracy on thin chains and gemstones is genuinely incredible.","Sarah K.","London, UK &#127468;&#127463;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","As a real estate photographer I need clean property images fast. PixCut removes distracting backgrounds from listing photos in seconds. I also use the object remover to fix minor issues I'd normally spend time on in Lightroom.","James T.","Chicago, USA &#127482;&#127480;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I used PixCut's AI Headshot Generator from a regular selfie. I now use it as my LinkedIn photo. Three colleagues asked which studio I used. Saved me $300. I've also used it for my company About page.","Priya M.","Mumbai, India &#127470;&#127475;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Ich verkaufe Mode auf Amazon. Jedes Produktfoto braucht wei&#223;en Hintergrund. PixCut macht das in Sekunden &#8212; perfekte Kanten sogar bei d&#252;nner Spitze und Mesh-Stoff. Spart mir jeden Tag mehrere Stunden.","Klaus B.","Berlin, Deutschland &#127465;&#127466;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","The 8x upscaler saved a complete product reshooting session. I had old low-resolution photos from 5 years ago &#8212; PixCut upscaled them to usable quality. The AI adds genuine sharpness, not just blurry enlarged pixels.","Tom H.","Sydney, Australia &#127462;&#127482;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","J'utilise PixCut pour tous mes visuels Instagram. La suppression de fond est parfaite et les r&#233;sultats sont professionnels. Bien plus rapide et accessible que Photoshop pour ce que j'ai besoin au quotidien.","Marie D.","Paris, France &#127467;&#127479;"),
]

def TESTIMONIALS_GRID():
    cards="".join(f'<div class="tcard"><div class="stars">{s}</div><p class="ttext">"{t}"</p><div class="tauthor">{n} &#8212; {l}</div></div>' for s,t,n,l in TESTIMONIALS)
    return f'<div class="grid3">{cards}</div>'

FAQ_GLOBAL=[
    ("What is Wondershare PixCut?","Wondershare PixCut is an AI-powered online background remover that automatically removes backgrounds from any image in seconds. It also removes objects and watermarks, upscales images up to 8x, generates AI headshots from selfies and replaces backgrounds. Free to start, no installation required."),
    ("Is PixCut free to use?","Yes &#8212; PixCut has a free tier for background removal with standard resolution downloads and no watermarks. HD downloads and bulk processing beyond a few images require a paid plan."),
    ("How does PixCut remove backgrounds?","PixCut uses deep learning AI trained on millions of images to identify the foreground subject and separate it from the background automatically. Upload an image &#8212; AI does everything in under 10 seconds. No manual selection, no masking, no Photoshop skills required."),
    ("Does PixCut handle hair and fine detail accurately?","Yes &#8212; PixCut's AI is specifically trained on complex edge cases including hair, fur, fine jewellery chains, transparent objects and fabrics. It preserves natural edge textures rather than creating hard cutout lines."),
    ("Can I remove backgrounds from 20 images at once?","Yes &#8212; PixCut's bulk processing handles up to 20 images simultaneously. Upload a batch, AI processes all in parallel, download as a ZIP. For 200 product images, this is 10 batches &#8212; completed in approximately 20-30 minutes."),
    ("Does PixCut need installation?","No &#8212; PixCut is web-based and works in any browser on any device. No download, no installation. iOS and Android apps are also available for mobile use."),
    ("Can I replace backgrounds after removing them?","Yes &#8212; PixCut's Background Replacer lets you add solid colours (including pure white for ecommerce), upload a custom background image, or choose from PixCut's built-in background library."),
    ("What does the 8x image upscaler do?","PixCut's AI upscaler enlarges images up to 8x the original size while adding genuine detail rather than just stretching pixels. It produces sharper, more detailed images at larger sizes &#8212; useful for old product photos, scanned images and low-resolution photos."),
    ("What is the AI Headshot Generator?","PixCut's AI Headshot Generator transforms a regular selfie into a professional headshot-style portrait suitable for LinkedIn, CVs and company profiles. Multiple professional styles are available."),
    ("How does PixCut compare to Remove.bg?","PixCut matches Remove.bg's background removal quality and adds features Remove.bg lacks: object and watermark removal, 8x image upscaler, AI headshot generator and background replacer. PixCut's free tier is also more generous with downloads."),
    ("Does PixCut have a developer API?","Yes &#8212; PixCut provides a REST API for developers to integrate background removal into their own applications. The API supports high-volume processing and commercial use."),
    ("Can I use PixCut results commercially?","Yes &#8212; images processed with PixCut can be used for commercial purposes including product listings, advertising, marketing materials and client work."),
]

def FAQ_BLOCK(pairs):
    items="".join(f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q,a in pairs)
    return f'<div class="faq-list">{items}</div>'

def related_cloud(kw_data,n=24):
    same=[k for k in KEYWORDS if k["cat"]==kw_data["cat"] and k["slug"]!=kw_data["slug"]]
    diff=[k for k in KEYWORDS if k["cat"]!=kw_data["cat"]]
    pool=(same+diff)[:n]
    links="".join(f'<a class="kw" href="{BASE_PATH}/{r["slug"]}.html">{r["keyword"]}</a>' for r in pool)
    return f'<div class="kw-cloud">{links}</div>'

def cat_deep(cat,keyword):
    a1,_ = ac(cat)
    bodies={
"background-removal":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">How AI Background Removal Works</div><h2>The Technology Behind PixCut\'s Accuracy</h2>'
    '<div class="prose">'
    '<p>Traditional background removal required either manually drawing around a subject in Photoshop &#8212; 5-15 minutes per image even for skilled editors &#8212; or using colour-based selection tools that fail the moment the background colour appears anywhere in the subject. PixCut\'s AI works fundamentally differently: it understands image content at a semantic level, identifying what the subject <em>is</em>, not just what colour it is.</p>'
    '<h3>Deep Learning for Semantic Understanding</h3>'
    '<p>PixCut\'s model is trained on hundreds of millions of images across all types of subjects &#8212; people, products, animals, objects, text, logos. The AI learns to recognise the boundary between subject and background even when colours are similar, even in complex scenes, and even with subjects that are inherently difficult like hair with dozens of individual strands.</p>'
    '<h3>Edge Accuracy &#8212; The Critical Difference</h3>'
    '<p>The quality of background removal is almost entirely determined by edge quality. A subject extracted with a hard, artificial edge looks clearly cut out. PixCut produces feathered, natural edges that match the original boundary of the subject &#8212; fine hair strands are individually preserved, soft fabric edges maintain their texture, and transparent materials are handled with accurate alpha values rather than being made fully opaque or fully removed.</p>'
    '<h3>Refine After AI</h3>'
    '<p>The Erase brush removes any background the AI kept. The Restore brush recovers any subject area the AI accidentally removed. These manual tools run at the same edge quality as the AI pass &#8212; producing smooth, natural results rather than the hard brush edges you\'d get in a basic photo editor.</p>'
    '</div></div></section>'),

"ecommerce":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Ecommerce Product Photo Guide</div><h2>Amazon-Compliant White Background Photos &#8212; Automated</h2>'
    '<div class="prose">'
    '<p>Amazon\'s main product image rules are strict: pure white background (RGB 255,255,255), product filling at least 85% of the image frame, no props, no additional text, no lifestyle elements. Similar requirements apply to Walmart Marketplace, eBay (recommended for search ranking), Shopify (for brand consistency) and Etsy. Every image in your product catalogue needs to meet this standard. PixCut handles this at scale.</p>'
    '<h3>The Scale Problem</h3>'
    '<p>A seller with 200 product SKUs, each needing 3-5 images, has 600-1,000 images to process. At 10 minutes per image in Photoshop, that is 100-170 hours of editing. At 3 months of evenings, or $3,000-5,000+ of paid editing time. PixCut\'s bulk processing handles 20 images in 1-2 minutes &#8212; the same 600 images in approximately 1-2 hours, with no prior skill required.</p>'
    '<h3>Difficult Product Categories</h3>'
    '<p><strong>Jewellery:</strong> Thin chains, small clasps, gemstone facets &#8212; all preserved accurately by PixCut\'s AI. <strong>Clothing:</strong> Fine lace, sheer fabric, mesh, embroidery &#8212; edges maintained without blocky masking artifacts. <strong>Glass and transparent products:</strong> Bottles, glasses, packaging &#8212; AI preserves transparency correctly. <strong>Electronics:</strong> Small components, reflective surfaces, antennas &#8212; handled with the same accuracy as simpler products.</p>'
    '<h3>From White Background to Lifestyle Images</h3>'
    '<p>After removing the background, PixCut\'s Background Replacer adds any context scene. A kitchen appliance on a kitchen counter. A cosmetics product on a marble surface. A clothing item on a lifestyle environment. This creates the full suite of product images &#8212; compliant white background for the marketplace main image, and lifestyle images for additional slots and social media &#8212; all from a single original photo with no second photoshoot.</p>'
    '</div></div></section>'),

"portrait-headshot":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Portrait &amp; Headshot Guide</div><h2>Professional Headshots &amp; Profile Photos &#8212; No Studio Needed</h2>'
    '<div class="prose">'
    '<p>Portrait background removal is the most technically demanding type of background removal. Hair &#8212; especially loose, curly or fine hair &#8212; is the hardest subject for any background removal algorithm. A person standing against a simple wall with straight dark hair is easy. A person with blonde curls against a textured background tests even the best tools. PixCut\'s portrait training data encompasses the full range of hair types, skin tones, lighting conditions and background complexities.</p>'
    '<h3>LinkedIn and Professional Profile Photos</h3>'
    '<p>A professional LinkedIn photo requires a neutral or solid background &#8212; white, light grey or a professional colour. With PixCut: take a photo anywhere with good natural light, upload to PixCut, remove the background, replace with white or neutral grey, download. The result is professional-quality for LinkedIn, company websites, team directories and conference speaker bios &#8212; without booking and attending a headshot session.</p>'
    '<h3>AI Headshot Generator &#8212; Beyond Background Removal</h3>'
    '<p>PixCut\'s AI Headshot Generator is more than a background removal tool. It takes a selfie and applies professional studio-style transformations: lighting optimisation, colour grading, focus depth simulation and multiple headshot style presets (formal business, creative professional, academic). The output looks like a professionally shot studio headshot &#8212; not just a selfie with the background removed. Multiple colleagues and clients routinely cannot tell the difference.</p>'
    '<h3>ID and Passport Photos</h3>'
    '<p>Passport photo requirements specify exact background colours (white or off-white for most countries). PixCut removes the original background and replaces with the exact colour specification. The photo must still meet other requirements (correct expression, lighting, no head coverings in most cases) but the background requirement is handled in seconds, at home, for free.</p>'
    '</div></div></section>'),

"bulk-processing":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Bulk Processing Guide</div><h2>20 Background Removals at Once &#8212; The Maths</h2>'
    '<div class="prose">'
    '<p>Single-image background removal takes PixCut\'s AI under 10 seconds. Bulk processing doesn\'t mean 20 times longer &#8212; it means 20 images processed in parallel, completing in 1-2 minutes total. The time per image in batch mode is essentially the same as single-image mode.</p>'
    '<h3>Time Saved at Scale</h3>'
    '<p>100 product images: Photoshop (10 min each) = 1,000 minutes (16+ hours). PixCut batch (20 at a time, 1-2 min per batch) = 5-10 minutes. 200 product images: Photoshop = 33+ hours. PixCut = approximately 15-20 minutes. For ecommerce businesses with large catalogues, this is not a convenience &#8212; it is the difference between a viable and an unviable production workflow.</p>'
    '<h3>Consistent Results Across the Catalogue</h3>'
    '<p>Manual background removal across a large catalogue produces inconsistent results &#8212; different editors, different sessions, different lighting produce varying edge treatment and output quality. PixCut\'s AI applies the same algorithm to every image, producing consistent edge quality and consistent transparency throughout the catalogue.</p>'
    '<h3>API for Unlimited Volume</h3>'
    '<p>The 20-image limit applies to the web interface batch mode. PixCut\'s REST API has no session limit &#8212; process thousands of images programmatically. Integrate the API into your product management system to trigger background removal automatically when new product photos are uploaded, with transparent PNG outputs delivered directly to your storage.</p>'
    '</div></div></section>'),

"object-removal":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Object Removal Guide</div><h2>Invisible Object, Watermark &amp; Defect Removal</h2>'
    '<div class="prose">'
    '<p>PixCut\'s Object Remover uses AI content-aware fill &#8212; the same technology found in Photoshop\'s Content-Aware Fill, but accessible in any browser, free to start. Paint over an object, watermark or defect with the removal brush, and AI fills the area with content that plausibly matches the surrounding pixels. The removal is invisible &#8212; no obvious patch, no blurred area, no colour mismatch.</p>'
    '<h3>Watermark Removal</h3>'
    '<p>Product images with visible watermarks, draft images with software trial watermarks, old photos with lab stamps, documents with text watermarks &#8212; all can be removed with the brush tool. The brush size adjusts for the watermark size. The AI analyses the pattern, texture and colours surrounding the watermark and fills the removed area with content that looks natural in context.</p>'
    '<h3>Object and Background Element Removal</h3>'
    '<p>A product photo with a stray packaging element in frame. A portrait with a distracting object in the background. A landscape with a person photobombing. PixCut\'s object removal handles these non-background-removal cases where you want to remove a specific element from within an otherwise good photo rather than the entire background.</p>'
    '<h3>Photo Defect and Damage Repair</h3>'
    '<p>Scanned physical photographs accumulate dust, scratches, foxing and physical damage over time. PixCut\'s defect remover treats each scratch or dust spot as an object to remove, filling with surrounding photographic content. For archiving family photos or restoring historical images, this provides accessible restoration without specialist photo editing skills.</p>'
    '</div></div></section>'),

"image-enhancement":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Image Enhancement Guide</div><h2>AI Upscaling &#8212; 8x Without Quality Loss</h2>'
    '<div class="prose">'
    '<p>Standard image enlargement simply replicates or interpolates pixels &#8212; making the image larger but blurrier. AI upscaling uses machine learning trained on millions of high-and-low-resolution image pairs to learn how to add plausible detail when making an image larger. The result is a bigger image that contains more genuine detail rather than the same detail spread across more pixels.</p>'
    '<h3>The 8x Upscaler in Practice</h3>'
    '<p>A 300x300 pixel product thumbnail upscaled 8x becomes 2,400x2,400 &#8212; sufficient for print and high-resolution digital use. A 1MP phone photo becomes a usable 8MP equivalent. Old product photos from 2015 cameras that are too small for modern marketplace requirements can be brought up to specification without reshooting.</p>'
    '<h3>Real Use Cases</h3>'
    '<p><strong>Old ecommerce catalogues:</strong> Products photographed when camera technology was limited can be brought to current resolution standards. <strong>Compressed web images:</strong> Images downloaded from social media or compressed for web use can be restored to better quality. <strong>Printed materials:</strong> Images that worked for digital screens but are too low-resolution for print can be upscaled for brochures, packaging and signage. <strong>Archival photos:</strong> Digitised physical photographs from older cameras can be enhanced for modern display.</p>'
    '<h3>Photo Enhancer &#8212; Beyond Upscaling</h3>'
    '<p>PixCut\'s Photo Enhancer applies adaptive AI corrections to blurry, hazy or poorly exposed images. Unlike fixed filters, the AI analyses each image individually and applies corrections &#8212; white balance adjustment, colour enhancement, sharpening, exposure compensation &#8212; calibrated to what that specific image needs. Good for photos taken in suboptimal conditions that have value but were never quite right.</p>'
    '</div></div></section>'),

"design-marketing":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Design &amp; Marketing Guide</div><h2>Background Removal for Creative and Marketing Workflows</h2>'
    '<div class="prose">'
    '<p>Background removal is one of the most repetitive production tasks in graphic design and marketing &#8212; isolating subjects for composites, creating transparent logo files, extracting product images for templates. Every minute spent on this task is a minute not spent on the creative decisions that require human judgment. PixCut automates the repetitive extraction, delivering consistent transparent PNGs at production speed.</p>'
    '<h3>Brand Asset Library &#8212; Transparent PNG Everything</h3>'
    '<p>Logos, product images, spokesperson photos, icons &#8212; every brand asset should exist as a transparent PNG for flexible use on any background colour, in any template, on any medium. PixCut processes the full brand asset library in one batch session, converting every JPEG or white-background PNG to a properly transparent version ready for any design context.</p>'
    '<h3>Social Media Content at Scale</h3>'
    '<p>Content calendars require isolated subject images for branded templates. A week\'s content requires 7-14 isolated images. PixCut batch removes backgrounds from the week\'s content batch in minutes, feeding directly into Canva, Adobe Express or Figma template workflows. The API integration can make this fully automated &#8212; new photos added to a folder automatically produce transparent PNG outputs.</p>'
    '<h3>YouTube Thumbnail Production</h3>'
    '<p>High-performing YouTube thumbnails almost universally feature an isolated person or product against a bold, high-contrast background. PixCut removes backgrounds from presenter photos or product shots, which are then placed on thumbnail templates in any design tool. Batch processing handles thumbnail assets for an entire upload schedule in one session.</p>'
    '</div></div></section>'),

"api-developer":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Developer API Guide</div><h2>PixCut Background Removal API &#8212; For Developers</h2>'
    '<div class="prose">'
    '<p>PixCut\'s REST API makes the same AI background removal available programmatically. Send an image to the API endpoint, receive a transparent PNG. Integrate into any language, any platform, any workflow. No UI required &#8212; the API handles background removal at any volume without manual interaction.</p>'
    '<h3>When to Use the API</h3>'
    '<p><strong>Ecommerce platforms:</strong> Automatically remove backgrounds when sellers upload product photos. Deliver marketplace-compliant white background images instantly without seller action. <strong>Photo editing apps:</strong> Add background removal as a one-click feature to your editing application without building the AI from scratch. <strong>CMS/DAM integration:</strong> Automatically produce transparent PNG versions of every image uploaded to a content management or digital asset management system. <strong>Automated pipelines:</strong> Trigger background removal as part of a photo processing pipeline for high-volume photography operations.</p>'
    '<h3>API vs Web Interface &#8212; When to Use Each</h3>'
    '<p>Web interface: Occasional manual use, up to 20 images at a time, no coding required. API: Automated workflows, high volume (hundreds or thousands per day), integration into existing software, programmatic access. The API supports the same AI quality as the web interface &#8212; same model, same edge accuracy, same output specification.</p>'
    '<h3>Pricing Compared to Remove.bg API</h3>'
    '<p>Remove.bg is the most well-known background removal API. PixCut\'s API offers comparable quality at competitive pricing, with the additional capability of object removal and enhancement features available through the same API. For developers evaluating background removal API options, PixCut is worth including in any pricing comparison.</p>'
    '</div></div></section>'),

"compare":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Honest Comparison</div><h2>'+keyword+' &#8212; Detailed Analysis</h2>'
    '<div class="prose">'
    '<p>Background removal tools vary significantly in quality, features and pricing. Here is the honest comparison most review sites don\'t provide.</p>'
    '<h3>vs Remove.bg</h3>'
    '<p>Remove.bg is the reference-standard background remover &#8212; strong AI, clean edges, widely used. PixCut matches its core removal quality and adds: object and watermark removal (Remove.bg has no equivalent), 8x upscaler (Remove.bg has no upscaler), AI headshot generator (Remove.bg has no headshot feature) and a more generous free tier. For background-removal-only use, they\'re comparable. For users needing more, PixCut is more complete.</p>'
    '<h3>vs Canva Pro Background Remover</h3>'
    '<p>Canva Pro costs $13+/month and background removal only works inside Canva\'s design editor &#8212; you can\'t use it standalone. PixCut works on any image independently of any design tool, handles complex subjects more accurately, and doesn\'t require a design subscription.</p>'
    '<h3>vs Adobe Photoshop</h3>'
    '<p>Photoshop\'s background removal is excellent but requires a $21+/month Creative Cloud subscription, desktop installation, and significant skill. PixCut achieves comparable results in any browser, free to start, in under 10 seconds, with zero learning curve. For background removal specifically, PixCut is faster and more accessible for the vast majority of use cases.</p>'
    '</div></div></section>'),

"social-proof":(
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Real-World Results</div><h2>What Real PixCut Users Achieve</h2>'
    '<div class="prose">'
    '<p>The most meaningful test of any tool is what real users produce with it. PixCut is used daily by ecommerce sellers, graphic designers, photographers, content creators, businesses and individuals across every industry. The use cases that come up most consistently reveal where PixCut genuinely delivers.</p>'
    '<h3>Ecommerce Sellers &#8212; The Time Saving</h3>'
    '<p>Sellers consistently report 80-90% time reduction on product photo background removal. An operation that required 10 minutes per image in Photoshop now takes under 30 seconds per image including download time. For sellers with large catalogues, this represents hundreds of hours per year returned to selling, sourcing and customer service rather than photo editing.</p>'
    '<h3>The AI Headshot &#8212; The Social Test</h3>'
    '<p>The most frequently cited user story for the AI Headshot Generator: the professional who couldn\'t immediately book a photography session, used PixCut, and found that colleagues, recruiters and potential clients not only accepted the headshot but actively complimented it. The AI\'s professional lighting simulation and style presets produce results that pass social scrutiny in professional contexts.</p>'
    '<h3>Accuracy on Difficult Subjects</h3>'
    '<p>The subjects that trip up free tools &#8212; long curly hair, transparent cosmetics packaging, thin jewellery chains, fine lace fabric &#8212; are consistently highlighted by PixCut users as producing surprisingly accurate results. The AI training specifically targets these difficult categories, which is why accuracy on them significantly exceeds what older colour-based tools or basic AI models produce.</p>'
    '</div></div></section>'),
    }
    body=bodies.get(cat)
    if body: return body
    return (f'<section style="background:#fff"><div class="container">'
            f'<div class="sec-ey">Complete Guide</div>'
            f'<h2>{keyword} &#8212; Overview</h2>'
            f'<div class="prose">'
            f'<p>Wondershare PixCut is the leading solution for {keyword.lower()}. '
            f'AI background removal works on any image in seconds &#8212; no Photoshop, no installation, free to start. '
            f'Bulk removal up to 20 images, object and watermark remover, 8x upscaler and AI headshot generator included.</p>'
            f'<p>Whether you\'re an ecommerce seller, designer, photographer or someone who just needs a clean background-free image, '
            f'PixCut handles every scenario in one browser-based tool &#8212; Windows, Mac, Android or iPhone.</p>'
            f'</div>'
            f'<div style="margin-top:2rem">'
            f'<a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
            f'</div></div></section>')

def build_keyword_page(kw_data):
    slug=kw_data["slug"]; keyword=kw_data["keyword"]; cat=kw_data["cat"]
    a1,a2=ac(cat)
    title  = f"{keyword} &#8212; Wondershare PixCut | {YEAR}"
    desc   = f"Looking for {keyword.lower()}? PixCut removes image backgrounds with AI in seconds. Free to start, bulk 20 images, no install needed."
    canon  = f"{slug}.html"
    faq_pairs=[
        (f"Can PixCut handle {keyword.lower()}?",
         f"Yes &#8212; PixCut is built for {keyword.lower()}. "
         "AI removes backgrounds from any image instantly with accurate edges including hair and fine detail. "
         "Free to start, bulk processing up to 20 images, no installation needed."),
        ("Is PixCut free for this?",
         "Yes &#8212; PixCut has a free tier with standard resolution downloads and no watermarks. "
         "HD downloads and bulk processing require a paid plan."),
        ("Does it need installation?",
         "No &#8212; PixCut works in any browser on any device. No download or install required. "
         "iOS and Android apps are also available."),
    ]
    bc_s=BC_SCHEMA([("Home",""),("All Topics","keywords.html"),(keyword,"")])
    fq_s=FAQ_SCHEMA(faq_pairs)
    body=cat_deep(cat,keyword)
    same=[k for k in KEYWORDS if k["cat"]==cat and k["slug"]!=slug][:6]
    links=" &#183; ".join(f'<a href="{BASE_PATH}/{r["slug"]}.html">{r["keyword"]}</a>' for r in same)

    return (HEAD(title,desc,canon,bc_s+fq_s)
        +"\n<body>\n"
        +f"<style>:root{{--ha:{a1};--hb:{a2};--fa:rgba(0,0,0,.05)}}</style>\n"
        +NAV()+"\n"
        +BC([("Home",BASE_PATH+"/"),("All Topics",BASE_PATH+"/keywords.html"),(keyword,"")])
        +'\n<section class="hero">'
        +f'\n  <div class="eyebrow">&#10022; {cat.replace("-"," ").title()}</div>'
        +f'\n  <h1><em>{keyword}</em><br>&#8212; With PixCut</h1>'
        +'\n  <p class="hsub">AI-powered &#183; Instant &#183; Free to start &#183; Bulk 20 images &#183; No install</p>'
        +'\n  <div class="btns">'
        +f'\n    <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +f'\n    <a href="{BASE_PATH}/how-it-works.html" class="btn-s">How It Works</a>'
        +'\n  </div>'
        +'\n  <div class="stats">'
        +'\n    <div><span class="stat-n">AI</span><span class="stat-l">Powered</span></div>'
        +'\n    <div><span class="stat-n">Instant</span><span class="stat-l">Results</span></div>'
        +'\n    <div><span class="stat-n">Bulk 20</span><span class="stat-l">At Once</span></div>'
        +'\n    <div><span class="stat-n">Free</span><span class="stat-l">To Start</span></div>'
        +'\n  </div>\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">All Features</div><h2>Everything in PixCut</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +body
        +'\n<section style="background:#faf5ff"><div class="container"><div class="sec-ey">Real Users</div><h2>What People Say About PixCut</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        +FAQ_BLOCK(faq_pairs+FAQ_GLOBAL[:3])
        +f'\n  <div style="margin-top:1.5rem"><a href="{BASE_PATH}/faq.html" style="color:var(--ha);font-weight:600;font-size:.88rem">View all FAQs &#8594;</a></div>'
        +'\n</div></section>\n'
        +'\n<section class="dark-sec"><div class="container"><div class="sec-ey">Related Topics</div><h2>Explore More</h2>'
        +related_cloud(kw_data,28)
        +(f'\n  <p style="margin-top:1.4rem;font-size:.78rem;color:rgba(255,255,255,.35)">More: {links}</p>' if links else '')
        +'\n</div></section>\n'
        +CTA(f"Try PixCut for {keyword.title()} &#8212; Free","AI-powered, instant, free to start.")
        +"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")

def page_index():
    extra=FAQ_SCHEMA(FAQ_GLOBAL[:6])+BC_SCHEMA([("Home","")])
    uses=[
        ("&#9986;","Remove Background",   "remove-background-from-image",       "Any image, instant AI"),
        ("&#128230;","Bulk Removal",       "bulk-background-remover-online",      "Up to 20 images at once"),
        ("&#128247;","Remove Watermarks",  "remove-watermark-from-image-free",    "Objects, text, defects"),
        ("&#128200;","Upscale 8x",         "image-upscaler-online-free",          "No quality loss"),
        ("&#128736;","Product Photos",     "product-photo-background-remove",     "Ecommerce white backgrounds"),
        ("&#129312;","AI Headshots",       "ai-headshot-generator-free",          "Selfie to LinkedIn photo"),
        ("&#127800;","Logo Transparent",   "logo-background-remover-free",        "Clean transparent PNG"),
        ("&#127760;","Developer API",      "background-removal-api-free",         "Integrate into your app"),
    ]
    ug="".join(f'<a class="uc-card" href="{BASE_PATH}/{s}.html"><span class="uc-icon">{i}</span><span class="uc-label">{n}</span><span class="uc-sub">{d}</span></a>' for i,n,s,d in uses)
    return (HEAD(f"PixCut &#8212; AI Background Remover | Free | Bulk | 8x Upscaler | {YEAR}",
                 "AI removes image backgrounds in seconds. Bulk 20 images, watermark removal, 8x upscaler, AI headshots. Free to start, no install.",
                 "",extra)
        +"\n<body>\n"+NAV()
        +'\n<section class="hero">'
        +'\n  <div class="eyebrow">&#10022; AI Background Remover &#183; Free to Start &#183; No Install</div>'
        +'\n  <h1>Remove Backgrounds.<br><em>Instantly. Accurately. Free.</em></h1>'
        +'\n  <p class="hsub">AI removes image backgrounds in seconds &#8212; accurate edges including hair and fine detail. Bulk process 20 images, remove watermarks and objects, upscale up to 8x and generate AI headshots. No install, free to start.</p>'
        +'\n  <div class="btns">'
        +f'\n    <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +f'\n    <a href="{BASE_PATH}/how-it-works.html" class="btn-s">How It Works</a>'
        +'\n  </div>'
        +'\n  <div class="stats">'
        +'\n    <div><span class="stat-n">AI</span><span class="stat-l">Powered</span></div>'
        +'\n    <div><span class="stat-n">Bulk 20</span><span class="stat-l">Images at Once</span></div>'
        +'\n    <div><span class="stat-n">8x</span><span class="stat-l">Image Upscale</span></div>'
        +'\n    <div><span class="stat-n">Free</span><span class="stat-l">To Start</span></div>'
        +'\n  </div>\n</section>\n'
        +'\n<section style="background:#fff"><div class="container">'
        +'\n  <div class="sec-ey">What Do You Need?</div><h2>Every Image Task Covered</h2>'
        +'\n  <p class="sec-sub">Click your use case for a step-by-step guide &#8212; or try PixCut now.</p>'
        +f'\n  <div class="uc-grid">{ug}</div>'
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Complete Feature Suite</div>'
        +'\n  <h2>Background Removal Is Just the Start</h2>'
        +'\n  <p class="sec-sub">Remove, replace, bulk process, enhance, upscale and generate AI headshots &#8212; all free to start.</p>'
        +FEATURES_GRID()
        +f'\n  <div style="margin-top:2.5rem;text-align:center"><a href="{BASE_PATH}/features.html" style="color:var(--ha);font-weight:600">View full feature list &#8594;</a></div>'
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Why PixCut?</div>'
        +'\n  <h2>Better Than Photoshop for This</h2>'
        +'\n  <div class="grid3">'
        +'\n    <div class="card"><div class="fi">&#128640;</div><h3>50-100x Faster Than Photoshop</h3><p>Manual Photoshop background removal: 5-15 minutes per image. PixCut AI: under 10 seconds. For 100 product photos that\'s 8-25 hours vs 15 minutes. The maths is not subtle.</p></div>'
        +'\n    <div class="card"><div class="fi">&#129504;</div><h3>Zero Skill Required</h3><p>Photoshop masking takes years to learn. PixCut requires nothing &#8212; upload, AI removes, download. Anyone produces professional-quality results immediately.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128185;</div><h3>Free to Start</h3><p>Remove backgrounds and download standard resolution images &#8212; free, no watermarks. Upgrade for HD and unlimited bulk processing when you need it.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#faf5ff"><div class="container"><div class="sec-ey">Real Users</div>'
        +'\n  <h2 style="text-align:center;margin-bottom:2.5rem">Sellers, Designers, Creators &amp; Professionals</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">FAQ</div><h2>Common Questions About PixCut</h2>'
        +FAQ_BLOCK(FAQ_GLOBAL[:6])
        +f'\n  <div style="margin-top:1.5rem;text-align:center"><a href="{BASE_PATH}/faq.html" style="color:var(--ha);font-weight:600">View all {len(FAQ_GLOBAL)} FAQs &#8594;</a></div>'
        +'\n</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")

def page_features():
    bc=BC_SCHEMA([("Home",""),("Features","")])
    rows=[
        ("AI Background Removal",       "V","V","V","V","V"),
        ("Bulk Removal (20+ images)",   "V","V","Partial","V","Paid"),
        ("Hair/Fine Detail Accuracy",   "V","V","V","Partial","V"),
        ("Object/Watermark Remover",    "V","X","X","X","Paid"),
        ("Image Upscaler (to 8x)",      "V","X","X","X","X"),
        ("AI Headshot Generator",       "V","X","X","X","X"),
        ("Background Replacer",         "V","Partial","V","V","Paid"),
        ("Developer REST API",          "V","V","X","V","Paid"),
        ("Mobile App",                  "V","V","V","V","V"),
        ("No Install Needed",           "V","V","V","V","V"),
        ("Free Downloads, No WM",       "V","Limited","V","Limited","X"),
        ("Commercial Use",              "V","V","Paid","Paid","V"),
    ]
    tools=["PixCut &#10022;","Remove.bg","Canva Pro","Adobe Express","Photoshop"]
    hrow="<tr><th>Feature</th>"+"".join(('<th class="hl">' if i==0 else '<th>')+t+'</th>' for i,t in enumerate(tools))+"</tr>"
    def cell(v,i):
        if i==0: return f'<td class="ck" style="font-weight:700">{v}</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        return f'<td class="cp">{v}</td>'
    trows="".join("<tr>"+cell(r[0],-1)+"".join(cell(v,i) for i,v in enumerate(r[1:]))+"</tr>" for r in rows)
    return (HEAD(f"PixCut Features &#8212; Background Removal, Upscaler, AI Headshots | {YEAR}",
                 "Complete PixCut feature list vs Remove.bg, Canva Pro, Adobe Express and Photoshop. AI background removal, 8x upscaler, AI headshots.",
                 "features.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Features","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Complete Feature List</div>'
        +'\n  <h1>Everything PixCut<br><em>Can Do</em></h1>'
        +'\n  <p class="hsub">Background removal &#183; Bulk &#183; Object remove &#183; 8x upscale &#183; AI headshots &#8212; all free to start</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">All Features</div><h2>The Complete Toolkit</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">5-Tool Comparison</div><h2>PixCut vs Every Alternative</h2>'
        +f'\n  <div class="tbl-wrap"><table><thead>{hrow}</thead><tbody>{trows}</tbody></table></div>'
        +'\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial = Limited &#160; &#10008; Not available &#160; WM = Watermark</p>'
        +'\n</div></section>\n'
        +CTA("Try All Features Free","No credit card, no installation. Free to start right now.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_how_it_works():
    bc=BC_SCHEMA([("Home",""),("How It Works","")])
    return (HEAD(f"How PixCut Works &#8212; Remove Backgrounds in 3 Steps | {YEAR}",
                 "Remove image backgrounds with PixCut in 3 steps: upload, AI removes, download. Free, instant, works in any browser.",
                 "how-it-works.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("How It Works","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; 3 Steps, Under 30 Seconds</div>'
        +'\n  <h1>Remove Backgrounds in<br><em>3 Steps</em></h1>'
        +'\n  <p class="hsub">Upload &#8594; AI removes background &#8594; download transparent PNG. Under 30 seconds total.</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Single Image</div><h2>Remove a Background in 3 Steps</h2>'
        +'\n  <div class="steps">'
        +'\n    <div class="step"><div class="sn">1</div><h3>Upload Your Image</h3><p>Drag and drop, click Upload or paste a URL. Supports JPG, PNG, WebP and other formats. Works on any device in any browser &#8212; no account required.</p></div>'
        +'\n    <div class="step"><div class="sn">2</div><h3>AI Removes Background</h3><p>PixCut AI identifies the subject, traces edges including hair and fine detail, and removes the background. Takes under 10 seconds for most images.</p></div>'
        +'\n    <div class="step"><div class="sn">3</div><h3>Download or Replace</h3><p>Download the transparent PNG directly. Or use Background Replacer to add solid colour, custom image or background from PixCut\'s library.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Batch Mode</div><h2>Process 20 Images Simultaneously</h2>'
        +'\n  <div class="steps">'
        +'\n    <div class="step"><div class="sn">1</div><h3>Select Batch Mode</h3><p>Click the Batch tab and upload up to 20 images. Mix different image types &#8212; products, portraits, logos &#8212; in the same batch.</p></div>'
        +'\n    <div class="step"><div class="sn">2</div><h3>AI Processes All in Parallel</h3><p>All 20 images processed simultaneously. Complete results ready within 1-2 minutes regardless of the number of images.</p></div>'
        +'\n    <div class="step"><div class="sn">3</div><h3>Download All at Once</h3><p>Download each result individually or all as a ZIP. Repeat with the next batch for larger sets.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container" style="padding-top:0"><div class="sec-ey">Fine-Tuning</div><h2>Manual Refinement When Needed</h2>'
        +'\n  <div class="grid2">'
        +'\n    <div class="card"><div class="fi">&#9986;</div><h3>Erase Brush</h3><p>Paint over any background area the AI kept. Smooth, natural results &#8212; not the hard brush edges of basic tools.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128396;</div><h3>Restore Brush</h3><p>Recover any subject area the AI accidentally removed. Bring back hair, fine detail or any mistakenly removed area.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#faf5ff"><div class="container"><div class="sec-ey">Real Results</div><h2>What Users Create with PixCut</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +CTA("Try PixCut Free","No credit card, no installation. Start in seconds.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_faq():
    all_faqs=FAQ_GLOBAL+[
        ("Does PixCut work on logos with fine detail?","Yes &#8212; PixCut accurately removes backgrounds from logos including complex illustrated logos, gradient fills and fine-line detail. Output is a transparent PNG with clean edges."),
        ("Can PixCut handle glass and transparent products?","PixCut handles semi-transparent products with good accuracy. Pure glass or completely transparent products remain challenging for all AI tools, but for most common transparent elements like clear packaging, results are good."),
        ("Does PixCut add watermarks to free images?","No &#8212; standard resolution background-removed images download without watermarks on the free tier. HD downloads require a paid plan."),
        ("Is PixCut good for Amazon product photos?","Yes &#8212; PixCut is used specifically for Amazon product photo compliance. It removes backgrounds, applies pure white replacement (RGB 255,255,255) and handles all product types including jewellery, clothing and glass."),
        ("How does PixCut's API compare to Remove.bg's API?","PixCut's API offers comparable background removal quality at competitive pricing, with additional features (object removal, enhancement) available through the same API. For developers evaluating options, PixCut is worth comparing directly on pricing per image."),
        ("What image formats does PixCut accept?","JPG, PNG, WebP and other common image formats. Output is always transparent PNG."),
        ("Does the upscaler work on all image types?","Yes &#8212; the 8x upscaler works on any image type: product photos, portraits, landscapes, logos. Results are best on images that have clear subject matter (rather than pure abstract noise)."),
    ]
    fq=FAQ_SCHEMA(all_faqs)
    bc=BC_SCHEMA([("Home",""),("FAQ","")])
    return (HEAD(f"PixCut FAQ &#8212; {len(all_faqs)} Questions Answered | {YEAR}",
                 "Every PixCut question answered &#8212; background removal, bulk, ecommerce, upscaler, API, headshots and pricing.",
                 "faq.html",fq+bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("FAQ","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Complete FAQ</div>'
        +f'\n  <h1>Every PixCut Question<br><em>Answered</em></h1>'
        +f'\n  <p class="hsub">{len(all_faqs)} questions &#8212; background removal, bulk, ecommerce, upscaler, API and pricing.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">All {len(all_faqs)} Questions</div><h2>Complete FAQ</h2>'
        +FAQ_BLOCK(all_faqs)
        +'\n</div></section>\n'
        +CTA("Try PixCut Free &#8212; No Credit Card","No installation required. Start in any browser.")
        +"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")

def page_compare():
    bc=BC_SCHEMA([("Home",""),("Compare","")])
    rows=[
        ("AI Background Removal",       "V","V","V","V","V"),
        ("Bulk (20+ images)",           "V","V","Partial","V","Paid"),
        ("Object/Watermark Remover",    "V","X","X","X","Paid"),
        ("Image Upscaler (8x)",         "V","X","X","X","X"),
        ("AI Headshot Generator",       "V","X","X","X","X"),
        ("Background Replacer",         "V","Partial","V","V","Paid"),
        ("Developer API",               "V","V","X","V","Paid"),
        ("No Watermark Free",           "V","X","V","X","X"),
        ("No Install",                  "V","V","V","V","X"),
        ("Mobile App",                  "V","V","V","V","X"),
    ]
    tools=["PixCut &#10022;","Remove.bg","Canva Pro","Adobe Express","Photoshop"]
    hrow="<tr><th>Feature</th>"+"".join(('<th class="hl">' if i==0 else '<th>')+t+'</th>' for i,t in enumerate(tools))+"</tr>"
    def cell(v,i):
        if i==0: return f'<td class="ck" style="font-weight:700">{v}</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        return f'<td class="cp">{v}</td>'
    trows="".join("<tr>"+cell(r[0],-1)+"".join(cell(v,i) for i,v in enumerate(r[1:]))+"</tr>" for r in rows)
    comps=[
        ("vs Remove.bg","Remove.bg is the reference AI background remover &#8212; strong, accurate, widely used. PixCut matches its quality and adds: object/watermark removal (Remove.bg has no equivalent), 8x upscaler, AI headshot generator, and more generous free downloads without watermarks. For pure background removal, they're comparable. For users needing more, PixCut is the more complete tool."),
        ("vs Canva Pro Background Remover","Canva Pro costs $13+/month and background removal only works inside Canva's design editor. PixCut works standalone on any image, handles complex subjects &#8212; especially hair &#8212; with better accuracy, adds object removal and upscaling, and doesn't require a design subscription to access the core feature."),
        ("vs Adobe Photoshop","Photoshop achieves excellent background removal but requires a $21+/month Creative Cloud subscription, desktop installation on sufficient hardware, and significant skill investment. PixCut achieves comparable results in any browser in under 10 seconds, free to start, with zero learning curve. For background removal specifically, PixCut is faster and more accessible."),
        ("vs Adobe Express","Adobe Express has a simple background remover but requires an Adobe account, limited free tier and lacks bulk processing, object removal and upscaling. PixCut is free to start, works without signup, and includes a complete suite of image editing features beyond background removal."),
    ]
    comp_cards="".join(f'<div class="card"><h3>{n}</h3><p style="font-size:.87rem;color:var(--muted)">{d}</p></div>' for n,d in comps)
    return (HEAD(f"PixCut vs Remove.bg, Canva, Photoshop &amp; Adobe Express &#8212; Best BG Remover {YEAR}",
                 "Honest comparison: PixCut vs Remove.bg, Canva Pro, Adobe Express and Photoshop. Best AI background remover 2025.",
                 "compare.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Compare","")])
        +f'\n<section class="hero"><div class="eyebrow">&#10022; Comparison {YEAR}</div>'
        +'\n  <h1>PixCut vs<br><em>Every Alternative</em></h1>'
        +'\n  <p class="hsub">Honest comparison &#8212; accuracy, features, pricing and free tier generosity.</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Try PixCut Free</a>'
        +'\n</section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Feature Matrix</div><h2>Complete Comparison Table</h2>'
        +f'\n  <div class="tbl-wrap"><table><thead>{hrow}</thead><tbody>{trows}</tbody></table></div>'
        +'\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial = Limited &#160; &#10008; Not available</p>'
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Head-to-Head</div><h2>vs Each Alternative</h2>'
        +f'\n  <div class="grid2">{comp_cards}</div>'
        +'\n</div></section>\n'
        +'\n<section style="background:#faf5ff"><div class="container"><div class="sec-ey">What PixCut Has Uniquely</div><h2>Three Features No Competitor Matches</h2>'
        +'\n  <div class="grid3">'
        +'\n    <div class="card"><div class="fi">&#128200;</div><h3>8x Image Upscaler</h3><p>Remove.bg, Canva, Adobe Express and Photoshop have no standalone AI upscaler at this ratio. PixCut upscales to 8x with genuine AI detail &#8212; not just enlarged pixels.</p></div>'
        +'\n    <div class="card"><div class="fi">&#129312;</div><h3>AI Headshot Generator</h3><p>No major competitor includes an AI headshot generator. PixCut transforms a selfie into a professional LinkedIn-quality headshot &#8212; replacing a $200-500 photography session.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128247;</div><h3>Object &amp; Watermark Remover</h3><p>Remove.bg only removes backgrounds. PixCut also removes specific objects, watermarks, text and defects with AI content-aware fill &#8212; all in the same browser tool.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +CTA("The Most Complete AI Image Tool &#8212; Try Free","No credit card, no installation required.")
        +"\n"+FOOTER()+"\n</body></html>")

BLOG_POSTS=[
    {"slug":"remove-background-ai-complete-guide-2025","title":"AI Background Removal in 2025 &#8212; The Complete Guide","excerpt":"Everything you need to know about AI background removal — how it works, best tools and practical use cases.","cat":"Background Removal","read":"8 min","date":"2025-01-15",
     "body":"<h2>How AI Background Removal Works</h2><p>AI background removal uses deep learning models trained on millions of image pairs &#8212; images with and without backgrounds &#8212; to learn what the foreground subject is in any new image. Unlike older colour-based selection tools, AI understands image content: it identifies that a person is the subject of a portrait regardless of background colour, and separates that person from the background even when background colours appear in the subject (like a grey jacket against a grey wall).</p><h2>Why PixCut Produces Accurate Results</h2><p>Accuracy on complex subjects &#8212; hair, transparent objects, fine jewellery &#8212; is determined by training data. PixCut's model was trained specifically on these difficult categories, which is why it handles curly hair, thin chains and sheer fabric better than generic image segmentation models.</p><h2>The 3-Step Process</h2><ol><li>Upload any image to PixCut in any browser</li><li>AI removes the background in under 10 seconds</li><li>Download transparent PNG or replace with a new background</li></ol><h2>When to Use Which Tool</h2><p>PixCut: fast, free to start, all image types, bulk processing, object removal, upscaling. Photoshop: maximum control over complex composites. Canva: if you're already designing inside Canva. The right tool depends on volume, skill level and budget.</p>"},
    {"slug":"bulk-background-removal-guide-2025","title":"Bulk Background Removal &#8212; Remove 20 Backgrounds at Once","excerpt":"Process entire product catalogues in minutes instead of hours — the bulk background removal guide.","cat":"Bulk Processing","read":"7 min","date":"2025-02-10",
     "body":"<h2>The Time Maths</h2><p>Manual Photoshop: 10 minutes per image. 200 product images = 33 hours = 4 working days. PixCut bulk processing: 20 images per batch, 1-2 minutes per batch. 200 images = 10 batches = 15-20 minutes. The ROI of switching to bulk AI processing is immediate and significant.</p><h2>How Batch Mode Works</h2><ol><li>Go to PixCut and select the Batch tab</li><li>Upload up to 20 images (drag and drop supported)</li><li>AI processes all images in parallel</li><li>Download all results as a ZIP file</li><li>Repeat for the next 20</li></ol><h2>Tips for Best Batch Results</h2><p>Use consistent lighting across the batch &#8212; PixCut's AI performs best when the product is clearly the main subject. Avoid backgrounds that match the product colour where possible. JPEG quality 80%+ recommended for best edge accuracy.</p>"},
    {"slug":"product-photo-white-background-amazon-2025","title":"Amazon-Compliant White Background Product Photos &#8212; AI Guide","excerpt":"Meet Amazon's exact image requirements automatically with PixCut's AI background removal.","cat":"Ecommerce","read":"6 min","date":"2025-03-05",
     "body":"<h2>Amazon's Product Image Requirements</h2><p>Main product image: pure white background (RGB 255,255,255), product fills 85%+ of frame, no props, no text overlay, no borders. These requirements are enforced and non-compliant images are rejected or suppressed in search. PixCut meets all of them automatically.</p><h2>Steps for Amazon-Compliant Images</h2><ol><li>Upload product photo to PixCut</li><li>AI removes original background</li><li>Select white replacement background (pure white #FFFFFF)</li><li>Ensure product fills the frame appropriately</li><li>Download HD PNG or JPEG</li></ol><h2>Difficult Product Types</h2><p>Jewellery (thin chains, gemstones), clothing (sheer fabrics, lace), glass products, electronics with antenna or cable details &#8212; PixCut's AI handles all of these with specific training on difficult product categories.</p>"},
    {"slug":"ai-headshot-generator-guide-2025","title":"AI Headshot Generator &#8212; Professional Photo from a Selfie","excerpt":"Turn a regular selfie into a LinkedIn-ready professional headshot using PixCut's AI headshot generator.","cat":"AI Headshots","read":"6 min","date":"2025-04-12",
     "body":"<h2>What the AI Headshot Generator Does</h2><p>PixCut's AI Headshot Generator applies professional studio-style transformations to a selfie: lighting optimisation, colour grading, focus depth simulation and professional background styles. The output looks like a professionally shot studio headshot &#8212; not a selfie with the background swapped. Multiple style presets (formal business, creative, academic) allow different professional contexts.</p><h2>Best Input for Best Results</h2><ul><li>Clear photo of your face, forward-facing</li><li>Good natural light (window light works well)</li><li>Neutral expression or professional smile</li><li>No strong shadows across the face</li></ul><h2>Use Cases</h2><p>LinkedIn profile photo, company About Us page, speaker bio, conference badge, CV/resume, professional email signature. All benefit from a clean professional headshot. The AI Headshot Generator provides this without a $200-500 photography session.</p>"},
    {"slug":"remove-watermark-from-photo-guide","title":"How to Remove Watermarks from Photos Online Free","excerpt":"Remove watermarks, stamps and text from images using PixCut's AI object remover.","cat":"Object Removal","read":"5 min","date":"2025-05-20",
     "body":"<h2>How PixCut's Watermark Remover Works</h2><p>PixCut uses AI content-aware fill &#8212; the same technology as Photoshop's Content-Aware Fill, accessible in any browser. Paint over the watermark. AI analyses surrounding pixels and fills the removed area with content that plausibly matches the surrounding image. The removal is invisible &#8212; no blur, no obvious patch.</p><h2>Steps</h2><ol><li>Upload image to PixCut</li><li>Select Object Remover</li><li>Adjust brush size to match watermark</li><li>Paint over the watermark completely</li><li>AI fills the area invisibly</li><li>Download the cleaned image</li></ol><h2>What Watermark Removal Works Best On</h2><p>Text watermarks on photographic backgrounds, logo watermarks on product images, price tag stickers on product photos. Works less well on watermarks that cover complex, highly detailed areas where fill matching is harder.</p>"},
    {"slug":"image-upscaler-8x-guide","title":"AI Image Upscaler &#8212; Upscale Photos to 8x Without Quality Loss","excerpt":"Make small images larger without blurring — PixCut's AI adds genuine detail up to 8x the original size.","cat":"Image Enhancement","read":"6 min","date":"2025-06-15",
     "body":"<h2>Why AI Upscaling Is Different from Regular Enlargement</h2><p>Regular image enlargement interpolates pixels &#8212; creating a bigger image that looks blurry because no real detail was added. AI upscaling uses deep learning to add plausible detail based on training from millions of high-quality images. The output is genuinely sharper, not just larger.</p><h2>How PixCut's Upscaler Works</h2><ol><li>Upload your low-resolution image</li><li>Select Image Upscaler</li><li>Choose scale factor (up to 8x)</li><li>Download the enhanced high-resolution result</li></ol><h2>Real Use Cases</h2><p><strong>Old product catalogue:</strong> Products from 5-10 years ago photographed at lower resolution can be brought to current standards. <strong>Social media images:</strong> Low-quality images downloaded from platforms can be improved. <strong>Print materials:</strong> Web-resolution images upscaled for brochures, packaging and signage. <strong>Scanned photos:</strong> Physical photos digitised at limited resolution enhanced for display.</p>"},
    {"slug":"pixcut-vs-remove-bg-honest-comparison-2025","title":"PixCut vs Remove.bg &#8212; Honest Comparison 2025","excerpt":"Both are leading AI background removers. Here's what makes them different and which to choose.","cat":"Compare","read":"7 min","date":"2025-07-10",
     "body":"<h2>Background Removal Quality</h2><p>Both PixCut and Remove.bg use high-quality AI models trained specifically for background removal. Edge accuracy on hair, fur and fine detail is comparable between the two tools. Both significantly outperform colour-based selection tools and basic image editors.</p><h2>Where PixCut Goes Further</h2><p><strong>Object/watermark remover:</strong> PixCut has one. Remove.bg does not. <strong>8x image upscaler:</strong> PixCut has one. Remove.bg does not. <strong>AI headshot generator:</strong> PixCut has one. Remove.bg does not. <strong>Free tier generosity:</strong> PixCut allows more free downloads without watermarks than Remove.bg's limited free quota.</p><h2>Where They're Equal</h2><p>Background removal quality, API availability, mobile apps, bulk processing. For the core background removal task, both tools deliver equivalent quality.</p><h2>Verdict</h2><p>Pure background removal only: either tool works. Object removal, upscaling or headshots also needed: PixCut is the more complete solution.</p>"},
    {"slug":"transparent-logo-png-guide","title":"How to Make Your Logo Transparent &#8212; Remove White Background Free","excerpt":"Turn any logo into a transparent PNG in seconds — works on any logo type, free with PixCut.","cat":"Design & Marketing","read":"5 min","date":"2025-08-05",
     "body":"<h2>Why Logos Need Transparent Backgrounds</h2><p>A logo delivered as a JPEG or PNG with white background only works on white surfaces. A logo with transparent background works on any background &#8212; dark website headers, coloured templates, printed packaging, email signatures. Every logo should exist as a transparent PNG.</p><h2>Steps with PixCut</h2><ol><li>Upload the logo image to PixCut</li><li>AI removes white or coloured background automatically</li><li>Download as transparent PNG</li><li>Use on any background in any design tool</li></ol><h2>Complex Logo Types</h2><p>PixCut handles: illustrated logos with fine detail, logos with drop shadows (transparency preserved), gradient logos, logos with thin lines and small text, logos on coloured backgrounds (not just white). For most logo types, the AI removal is accurate enough to use directly without manual refinement.</p>"},
    {"slug":"product-photo-background-ecommerce","title":"Product Photo Backgrounds for Ecommerce &#8212; 2025 Guide","excerpt":"White backgrounds, lifestyle images and consistent product photos — AI tools for ecommerce sellers.","cat":"Ecommerce","read":"7 min","date":"2025-09-15",
     "body":"<h2>The Three Product Photo Types You Need</h2><p><strong>White background main image:</strong> Required for Amazon, eBay and most marketplace main images. Shows the product clearly without distraction. <strong>Lifestyle images:</strong> Product in context (kitchen appliance in a kitchen, clothing on a person). Used for additional marketplace images and social media. <strong>Detail images:</strong> Close-up on features, materials, scale indicators. PixCut creates all three from original photographs.</p><h2>Workflow</h2><ol><li>Photograph product (consistent lighting, neutral background)</li><li>Upload to PixCut batch mode (up to 20 at a time)</li><li>AI removes original background</li><li>Download white background versions for marketplace main images</li><li>Apply lifestyle backgrounds using PixCut's Background Replacer</li><li>All three image types from one photoshoot</li></ol>"},
    {"slug":"background-removal-for-social-media","title":"Background Removal for Social Media Content &#8212; Create at Scale","excerpt":"Professional, consistent social media images with clean backgrounds — PixCut workflow for creators.","cat":"Design & Marketing","read":"6 min","date":"2025-10-20",
     "body":"<h2>Why Clean Backgrounds Drive Engagement</h2><p>High-performing social media posts almost universally share a visual characteristic: clean, uncluttered subjects on simple or branded backgrounds. The subject is clear, the background doesn't compete for attention, and the overall image looks intentional and professional. PixCut makes this achievable for any image without design software.</p><h2>Instagram Workflow</h2><p>Remove backgrounds from product or portrait photos. Replace with consistent brand colours or backgrounds that match your feed aesthetic. Batch process a week of content in one session using PixCut's 20-image batch mode. Feed into Canva or Adobe Express templates for final design.</p><h2>YouTube Thumbnail Workflow</h2><p>Remove background from presenter or product photos. Layer over high-contrast thumbnail backgrounds with text overlays in any design tool. The isolated subject on a clear background is the foundation of the highest-CTR thumbnail style across most content categories.</p>"},
    {"slug":"pixcut-api-developer-guide","title":"PixCut API &#8212; Background Removal for Developers","excerpt":"Integrate AI background removal into your app with PixCut's REST API — guide for developers.","cat":"API & Developer","read":"7 min","date":"2025-11-10",
     "body":"<h2>When to Use the PixCut API</h2><p><strong>Ecommerce platforms:</strong> Automatically remove product photo backgrounds when sellers upload images &#8212; no manual processing step. <strong>Photo editing apps:</strong> Add one-click background removal powered by PixCut's AI to your existing application. <strong>DAM/CMS integration:</strong> Automatically generate transparent PNG versions of every image added to your asset library. <strong>High-volume pipelines:</strong> Process thousands of images per day programmatically without the 20-image web interface limit.</p><h2>API Integration Basics</h2><p>PixCut's REST API accepts image URLs or base64-encoded image data. The response returns the processed transparent PNG. Integration in any language takes hours rather than days. Documentation is available on the Wondershare developer portal.</p><h2>vs Remove.bg API Pricing</h2><p>Remove.bg is the incumbent background removal API. PixCut offers comparable quality at competitive pricing. For high-volume use cases where API cost per image is material, direct pricing comparison between the two is recommended before committing.</p>"},
    {"slug":"best-background-remover-no-watermark","title":"Best Free Background Removers Without Watermarks in 2025","excerpt":"Which free background removers actually let you download clean images without adding watermarks?","cat":"Compare","read":"6 min","date":"2025-12-01",
     "body":"<h2>The Watermark Problem</h2><p>Many background removal tools add watermarks to free downloads &#8212; forcing an upgrade before you can use the image. This is a significant limitation for users who only occasionally need background removal and don't want a subscription.</p><h2>PixCut: No Watermark on Free Downloads</h2><p>PixCut's free tier downloads standard resolution background-removed images without watermarks. Free plan limitations: standard (not HD) resolution, limited bulk processing. But the core output &#8212; a clean background-removed image &#8212; is watermark-free and usable.</p><h2>Comparison</h2><p>Remove.bg: watermarks on free downloads &#8212; upgrade required for clean files. Canva: watermarks on free tier &#8212; Canva Pro required. Adobe Express: limited free access. PixCut: clean standard resolution downloads on free tier. For users who need occasional background removal without paying, PixCut's free tier is the most generous major option.</p>"},
    {"slug":"passport-photo-background-removal","title":"Passport Photo Background &#8212; Remove and Replace Free Online","excerpt":"Create passport-compliant photos with the correct background colour — instant, free, online.","cat":"Portrait & Headshot","read":"5 min","date":"2026-01-15",
     "body":"<h2>Passport Photo Background Requirements</h2><p>Most countries require passport photos on a plain white or off-white background. Specific requirements vary: USA requires plain white. UK requires off-white or cream. Canada requires plain white. PixCut removes any existing background and replaces with the exact colour specification.</p><h2>Steps</h2><ol><li>Take a photo in good lighting with a neutral expression</li><li>Upload to PixCut</li><li>AI removes the background</li><li>Use Background Replacer to add the required white or off-white</li><li>Download the result</li></ol><h2>What PixCut Doesn't Handle</h2><p>PixCut handles the background colour requirement only. Other passport photo requirements &#8212; correct dimensions, neutral expression, no glasses, correct head position, appropriate lighting &#8212; must be correct in the original photo. PixCut focuses on the background specifically.</p>"},
    {"slug":"headshot-vs-ai-headshot-comparison","title":"Professional Photography vs AI Headshot Generator &#8212; 2025 Comparison","excerpt":"$0 selfie plus PixCut vs $300 headshot session — is the AI headshot good enough?","cat":"AI Headshots","read":"6 min","date":"2026-02-10",
     "body":"<h2>The Cost Comparison</h2><p>Professional headshot session: $150-500 depending on location, photographer and deliverables. PixCut AI Headshot Generator: free to start. The question is whether the AI result passes as professional in the contexts where headshots matter.</p><h2>Where AI Headshots Work Well</h2><p>LinkedIn profiles &#8212; the vast majority of LinkedIn viewers are looking at profile photos at thumbnail size. AI headshots at thumbnail scale are indistinguishable from studio shots. Company About pages, conference speaker bios, professional email signatures &#8212; all low-scrutiny contexts where the headshot needs to look professional rather than impressive. These represent the majority of real-world headshot use.</p><h2>Where Professional Photography Is Worth It</h2><p>Executive photography for major brand websites. High-scrutiny professional contexts like national publications. Physical print at large size. Situations where the photo is the centrepiece rather than supporting context. For these specific uses, professional photography remains the right choice.</p><h2>The Practical Recommendation</h2><p>Use PixCut's AI Headshot Generator for LinkedIn, company websites and professional profiles. Book a professional session when the stakes and scrutiny are genuinely high.</p>"},
    {"slug":"background-removal-photography-workflow","title":"PixCut for Photographers &#8212; Background Removal at Professional Scale","excerpt":"How professional photographers integrate PixCut into client delivery workflows.","cat":"Use Cases","read":"7 min","date":"2026-03-05",
     "body":"<h2>Portrait Photography &#8212; Composite Preparation</h2><p>Portrait photographers creating composite images &#8212; placing studio subjects into location backgrounds, or extracting subjects for marketing material templates &#8212; need clean isolated subject files. PixCut produces isolated portrait PNGs with accurate hair and skin edge detail. The Erase and Restore brushes provide refinement for any edge areas that need adjustment after the AI pass.</p><h2>Product Photography &#8212; Commercial Delivery</h2><p>Commercial product photography clients typically need two deliverable types: white background versions for ecommerce listings, and isolated transparent PNGs for marketing templates. PixCut produces both. Remove background, download transparent PNG. Apply white background, download for marketplace. Two deliverables in under a minute per image &#8212; a workflow that previously required separate Photoshop sessions.</p><h2>Real Estate Photography</h2><p>Real estate listing photos sometimes require sky replacement or virtual staging that begins with isolated architectural subjects. PixCut's background removal provides the initial extraction. The object remover handles minor cleanup of distracting elements (temporary signs, construction items) within the frame.</p>"},
]

def page_blog():
    bc=BC_SCHEMA([("Home",""),("Blog","")])
    cards="".join(
        f'<div class="card"><div class="badge">{p["cat"]}</div>'
        f'<h3 style="margin-top:.55rem;margin-bottom:.45rem;font-size:.97rem">'
        f'<a href="{BASE_PATH}/blog/{p["slug"]}.html" style="color:var(--ink)">{p["title"]}</a></h3>'
        f'<p style="font-size:.84rem;margin-bottom:.85rem">{p["excerpt"]}</p>'
        f'<div style="display:flex;justify-content:space-between;align-items:center">'
        f'<span style="font-size:.73rem;color:var(--muted)">{p["date"]} &#183; {p["read"]}</span>'
        f'<a href="{BASE_PATH}/blog/{p["slug"]}.html" style="font-size:.8rem;font-weight:600;color:var(--ha)">Read &#8594;</a>'
        f'</div></div>'
        for p in BLOG_POSTS)
    return (HEAD(f"PixCut Blog &#8212; Background Removal Guides &amp; Tutorials | {YEAR}",
                 "AI background removal guides &#8212; ecommerce, portraits, bulk processing, upscaling, API and design tutorials.",
                 "blog.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Blog","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Background Removal Guides</div>'
        +f'\n  <h1>Guides &amp;<br><em>Tutorials</em></h1>'
        +f'\n  <p class="hsub">{len(BLOG_POSTS)} in-depth articles for every PixCut use case.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">All {len(BLOG_POSTS)} Articles</div><h2>Background Removal Guides</h2>'
        +f'\n  <div class="grid3">{cards}</div>'
        +'\n</div></section>\n'
        +CTA("Ready to Remove Backgrounds?","Try PixCut free &#8212; no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_blog_post(post):
    bc=BC_SCHEMA([("Home",""),("Blog","blog.html"),(post["title"][:40]+"...","")])
    art=ART_SCHEMA(post["title"],post["excerpt"],post["date"])
    others=[p for p in BLOG_POSTS if p["slug"]!=post["slug"]][:3]
    rel="".join(f'<div class="card"><div class="badge">{p["cat"]}</div><h3 style="margin-top:.5rem;font-size:.93rem"><a href="{BASE_PATH}/blog/{p["slug"]}.html" style="color:var(--ink)">{p["title"]}</a></h3><p style="font-size:.82rem">{p["excerpt"]}</p></div>' for p in others)
    h=HEAD(f'{post["title"]} | PixCut Guide',post["excerpt"],f'blog/{post["slug"]}.html',bc+art,"article")
    return (h+"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Blog",BASE_PATH+"/blog.html"),(post["cat"],"")])
        +'\n<section class="hero" style="padding:3.5rem clamp(1rem,5vw,3rem) 3rem">'
        +f'\n  <div class="eyebrow">&#10022; {post["cat"]} &#183; {post["read"]}</div>'
        +f'\n  <h1 style="font-size:clamp(1.7rem,4vw,2.8rem)">{post["title"]}</h1>'
        +f'\n  <p class="hsub" style="font-size:1rem">{post["excerpt"]}</p>'
        +f'\n  <p style="color:rgba(255,255,255,.38);font-size:.76rem">Published {post["date"]}</p>'
        +'\n</section>\n'
        +'\n<section style="background:#fff"><div class="container"><div style="max-width:780px">'
        +f'\n  <div class="prose">{post["body"]}</div>'
        +f'\n  <div class="notice" style="margin-top:2.5rem"><strong>Try PixCut free.</strong> AI background removal, bulk processing and more. '
        +f'\n    <a href="{AFFILIATE_URL}" target="_blank" rel="nofollow sponsored" style="color:var(--ha);font-weight:600">Get started &#8594;</a>'
        +'\n  </div></div></div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">More Guides</div><h2>Related Articles</h2>'
        +f'\n  <div class="grid3">{rel}</div>'
        +'\n</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n</body></html>")

def page_glossary():
    terms=[
        ("Background Removal","The process of separating a photo subject from its background. AI tools like PixCut do this automatically in seconds."),
        ("Transparent Background","A PNG where the background area has no colour &#8212; transparent rather than white. Allows placement on any background in design tools."),
        ("PNG Format","Portable Network Graphics. Supports transparency, making it the standard output for background-removed images."),
        ("AI Background Removal","Machine learning that automatically detects and removes image backgrounds. More accurate than colour-based selection tools."),
        ("Content-Aware Fill","AI technique that fills a removed area with content matching surrounding pixels. Used in PixCut's object and watermark remover."),
        ("Bulk Processing","Removing backgrounds from multiple images simultaneously. PixCut handles up to 20 images in one batch."),
        ("Object Remover","Removes specific objects, watermarks, text or defects from within a photo using AI content-aware fill."),
        ("Image Upscaling","Making an image larger. AI upscaling adds genuine detail rather than just stretching pixels."),
        ("8x Upscaler","PixCut's image upscaler that increases image dimensions to 8x the original while adding genuine AI-generated detail."),
        ("AI Headshot Generator","Transforms a selfie into a professional headshot-style portrait. PixCut's generator produces LinkedIn-quality results."),
        ("Background Replacer","Adds a new background to an image after the original was removed. PixCut supports solid colours, custom images and a library."),
        ("Erase Brush","Manual tool in PixCut for removing background areas the AI kept. Provides precision cleanup after the AI pass."),
        ("Restore Brush","Manual tool in PixCut for recovering subject areas accidentally removed by the AI."),
        ("Edge Accuracy","How precisely the boundary between subject and background is detected. High accuracy preserves natural details like hair."),
        ("Feathered Edge","Soft, graduated edge between subject and background. AI removal creates feathered rather than hard-cut edges."),
        ("White Background","RGB 255,255,255 background. Required by Amazon and most ecommerce platforms for main product images."),
        ("REST API","Programming interface that allows developers to integrate PixCut's background removal into their own applications via code."),
        ("Commercial Use","Using PixCut output for business: product listings, marketing, client work. Permitted under PixCut's licensing terms."),
        ("JPG/JPEG","Common compressed image format. PixCut accepts JPG input and outputs PNG with transparency."),
        ("WebP","Modern web image format. PixCut accepts WebP images for processing."),
        ("Hair Masking","Background removal around hair &#8212; the most technically challenging type. PixCut's AI is specifically trained on complex hair."),
        ("Batch Mode","PixCut's feature for processing multiple images at once &#8212; up to 20 images in a single session."),
        ("Photo Enhancer","PixCut feature that applies AI-adaptive corrections to blurry, hazy or poorly exposed images."),
        ("HEIC Format","iPhone photo format. PixCut accepts HEIC images and converts to standard formats during processing."),
        ("Alpha Channel","The transparency data in a PNG file that defines which areas are transparent. Background-removed PNGs have alpha channel data."),
    ]
    cards="".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t,d in terms)
    bc=BC_SCHEMA([("Home",""),("Glossary","")])
    return (HEAD(f"Background Removal Glossary &#8212; {len(terms)} Terms | {YEAR}",
                 "Complete background removal glossary &#8212; AI, transparent PNG, bulk, upscaling, API and design terms defined.",
                 "glossary.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Glossary","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Image Editing Reference</div>'
        +'\n  <h1>Background Removal<br><em>Glossary</em></h1>'
        +f'\n  <p class="hsub">{len(terms)} plain-language definitions for every image editing and AI term.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">{len(terms)} Terms</div><h2>Complete Glossary</h2>'
        +f'\n  <div class="grid3">{cards}</div>'
        +'\n</div></section>\n'
        +CTA("Ready to Remove Backgrounds?","Try PixCut free &#8212; no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_download():
    bc=BC_SCHEMA([("Home",""),("Try Free","")])
    return (HEAD(f"Try PixCut Free &#8212; AI Background Remover Online | {YEAR}",
                 "Try Wondershare PixCut free. AI background removal, bulk 20 images, object remover, 8x upscaler. Free to start, no install.",
                 "download.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Try Free","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Free to Start</div>'
        +'\n  <h1>Try PixCut<br><em>Free Right Now</em></h1>'
        +'\n  <p class="hsub">AI background removal &#8212; free to start, no credit card, no installation. Works in any browser instantly.</p>'
        +f'\n  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored" style="font-size:1.1rem;padding:1rem 2.5rem">&#8659; Try PixCut Free</a>'
        +'\n  <p style="color:rgba(255,255,255,.38);font-size:.78rem;margin-top:1rem">No installation &#183; Any browser &#183; Windows, Mac, Android &amp; iOS</p>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">What You Get Free</div><h2>PixCut Free Tier</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Access Options</div><h2>Use PixCut Your Way</h2>'
        +'\n  <div class="grid3">'
        +'\n    <div class="card"><h3>&#127760; Web Browser</h3><p>PixCut.wondershare.com works in Chrome, Firefox, Safari, Edge and any modern browser. No download. Open and start immediately.</p></div>'
        +'\n    <div class="card"><h3>&#128241; Mobile Apps</h3><p>iOS and Android apps for on-the-go background removal. Same AI quality as the web version. Available in the App Store and Google Play.</p></div>'
        +'\n    <div class="card"><h3>&#128736; Developer API</h3><p>REST API for programmatic integration into your own applications. Documentation available for all major languages.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +CTA("Try PixCut Free Now","No credit card &#183; No installation &#183; Instant results in any browser.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_keywords():
    cats=defaultdict(list)
    for k in KEYWORDS: cats[k["cat"]].append(k)
    sections=""
    for cat in sorted(cats.keys()):
        items=cats[cat]; desc=CAT_DESC.get(cat,""); a1,_=ac(cat)
        links="".join(f'<a class="kw" href="{BASE_PATH}/{k["slug"]}.html">{k["keyword"]}</a>' for k in items)
        sections+=(f'<div style="margin-bottom:3rem"><h3 style="font-size:1rem;font-weight:700;color:{a1};margin-bottom:.35rem;border-bottom:2px solid {a1};padding-bottom:.35rem;display:inline-block">{cat.replace("-"," ").title()} <span style="color:var(--muted);font-weight:400;font-size:.83rem">({len(items)})</span></h3>'
                   +(f'<p style="font-size:.82rem;color:var(--muted);margin:.45rem 0 .7rem;max-width:600px">{desc}</p>' if desc else '')
                   +f'<div class="kw-cloud">{links}</div></div>')
    bc=BC_SCHEMA([("Home",""),("All Topics","")])
    return (HEAD(f"PixCut &#8212; All {len(KEYWORDS)} Topics | {YEAR}",
                 "Browse all PixCut topics &#8212; background removal, bulk, ecommerce, portraits, upscaling, API and more.",
                 "keywords.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("All Topics","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Topic Directory</div>'
        +'\n  <h1>All Background Removal<br><em>Topics</em></h1>'
        +f'\n  <p class="hsub">{len(KEYWORDS)} targeted topics for every PixCut use case.</p>'
        +'\n</section>\n'
        +f'\n<section><div class="container"><div class="sec-ey">Browse All {len(KEYWORDS)} Topics</div>{sections}</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n</body></html>")

def page_privacy():
    bc=BC_SCHEMA([("Home",""),("Privacy","")])
    return (HEAD("Privacy Policy &#8212; PixCut Guide","Privacy policy for PixCut affiliate guide website.","privacy.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Privacy Policy","")])
        +'\n<section class="hero" style="padding:3.5rem 2rem 3rem"><div class="eyebrow">Legal</div><h1>Privacy <em>Policy</em></h1></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="prose" style="max-width:800px">'
        +f'\n  <p><strong>Last updated: {BUILD_DATE}</strong></p>'
        +'\n  <h3>1. About</h3><p>Affiliate promotional site for Wondershare PixCut AI background remover. We do not collect personal data beyond standard server logs.</p>'
        +'\n  <h3>2. Affiliate Disclosure</h3><p>Links on this site are affiliate links. When you purchase via our links, we may earn a commission at no extra cost to you.</p>'
        +'\n  <h3>3. Cookies</h3><p>This website does not use tracking cookies.</p>'
        +'\n  <h3>4. External Links</h3><p>Purchase links go to the official Wondershare website. We are not responsible for external site privacy practices.</p>'
        +'\n</div></div></section>\n'+FOOTER()+"\n</body></html>")

def page_404():
    return (f"<!DOCTYPE html>\n<html lang=\"en\"><head>\n<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>Page Not Found &#8212; PixCut</title>\n"
            f"<meta http-equiv=\"refresh\" content=\"4;url={SITE_DOMAIN}/\"/>\n"
            "<style>body{font-family:system-ui,sans-serif;background:#1e1b4b;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;margin:0;padding:2rem}"
            "h1{font-size:3rem;margin-bottom:.75rem;font-weight:800}p{color:rgba(255,255,255,.6);margin-bottom:2rem;line-height:1.6}"
            "a{background:#7c3aed;color:#fff;padding:.85rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700}</style>"
            f"</head><body><div><div style=\"font-size:4rem;margin-bottom:1rem\">&#9986;</div><h1>Page Not Found</h1>"
            f"<p>Redirecting to homepage in 4 seconds...</p><a href=\"{SITE_DOMAIN}/\">Go to PixCut Home</a></div></body></html>")

def build_sitemap():
    essential=[("",1.0,"weekly"),("features.html",.9,"monthly"),("how-it-works.html",.9,"monthly"),
               ("faq.html",.85,"monthly"),("compare.html",.85,"monthly"),("blog.html",.85,"weekly"),
               ("download.html",.9,"monthly"),("keywords.html",.8,"monthly"),
               ("glossary.html",.75,"monthly"),("privacy.html",.3,"yearly")]
    urls=""
    for path,pri,freq in essential:
        loc=SITE_DOMAIN+("/"+path if path else "/")
        urls+=f"  <url><loc>{loc}</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>\n"
    for p in BLOG_POSTS:
        urls+=f"  <url><loc>{SITE_DOMAIN}/blog/{p['slug']}.html</loc><lastmod>{p['date']}</lastmod><changefreq>monthly</changefreq><priority>0.75</priority></url>\n"
    for k in KEYWORDS:
        urls+=f"  <url><loc>{SITE_DOMAIN}/{k['slug']}.html</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>monthly</changefreq><priority>0.65</priority></url>\n"
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>'

def build_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /build-report.json\nSitemap: {SITE_DOMAIN}/sitemap.xml\n"

def build_llms():
    cats=sorted(set(k["cat"] for k in KEYWORDS))
    sample=", ".join(k["keyword"] for k in KEYWORDS[:30])
    return (f"# Wondershare PixCut\n\n"
            "> AI-powered online background remover. Removes backgrounds from any image in seconds. Free to start, no install.\n\n"
            "## Key Features\n"
            "- AI background removal: instant, accurate including hair and fine detail\n"
            "- Bulk processing: up to 20 images simultaneously\n"
            "- Object and watermark remover: AI content-aware fill\n"
            "- Image upscaler: up to 8x without quality loss\n"
            "- Background replacer: solid colour, custom or library\n"
            "- AI headshot generator: selfie to professional LinkedIn headshot\n"
            "- Developer REST API: integrate into any application\n"
            "- Web-based: no install, any browser, Windows/Mac/iOS/Android\n\n"
            "## Pricing\nFree tier: standard resolution downloads, no watermarks. Paid: HD, unlimited bulk.\n\n"
            f"## Try Free\n{AFFILIATE_URL}\n\n"
            "## Developer\nWondershare Technology Co., Ltd.\n\n"
            f"## Site\n{SITE_DOMAIN}\n"
            f"{len(KEYWORDS)} keyword pages &#183; {len(BLOG_POSTS)} blog posts &#183; {len(cats)} categories\n"
            f"Sitemap: {SITE_DOMAIN}/sitemap.xml\n\n"
            f"## Categories\n{', '.join(c.title() for c in cats)}\n\n"
            f"## Sample Keywords\n{sample}\n")

WORKFLOW="""name: Build & Deploy PixCut

on:
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Remove all old files from repo
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          find . -maxdepth 1 -type f ! -name 'build.py' ! -name 'README.md' -delete
          find . -maxdepth 1 -type d ! -name '.' ! -name '.git' ! -name '.github' -exec rm -rf {} + 2>/dev/null || true
          git add -A
          git diff --staged --quiet || git commit -m "Clean up old files"
          git push origin main

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run build script
        run: python3 build.py

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

def progress(i,total,label=""):
    pct=i/total; bar="█"*int(30*pct)+"░"*(30-int(30*pct))
    print(f"\r  [{bar}] {i:>4}/{total} {label:<42}",end="",flush=True)

def main():
    os.makedirs(DIST,exist_ok=True)
    os.makedirs(DIST+"/blog",exist_ok=True)
    os.makedirs(DIST+"/.github/workflows",exist_ok=True)

    print(f"\n{'═'*60}")
    print(f"  PixCut Site Builder v2 — {BUILD_DATE}")
    print(f"{'═'*60}")
    print(f"  Domain:   {SITE_DOMAIN}")
    print(f"  Keywords: {len(KEYWORDS)}")
    print(f"  Blog:     {len(BLOG_POSTS)} posts")
    print(f"{'═'*60}\n")

    essential={
        "index.html":        page_index(),
        "features.html":     page_features(),
        "how-it-works.html": page_how_it_works(),
        "faq.html":          page_faq(),
        "compare.html":      page_compare(),
        "blog.html":         page_blog(),
        "download.html":     page_download(),
        "keywords.html":     page_keywords(),
        "glossary.html":     page_glossary(),
        "privacy.html":      page_privacy(),
        "404.html":          page_404(),
    }
    print("  Essential pages:")
    for fname,html in essential.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(html)
        print(f"    ✓ {fname}  ({len(html)//1024}KB)")

    print(f"\n  Blog posts ({len(BLOG_POSTS)}):")
    for post in BLOG_POSTS:
        with open(DIST+"/blog/"+post["slug"]+".html","w",encoding="utf-8") as f:
            f.write(page_blog_post(post))
        print("    ✓ blog/"+post["slug"]+".html")

    print(f"\n  Keyword pages ({len(KEYWORDS)}):")
    for i,kw_data in enumerate(KEYWORDS):
        with open(DIST+"/"+kw_data["slug"]+".html","w",encoding="utf-8") as f:
            f.write(build_keyword_page(kw_data))
        progress(i+1,len(KEYWORDS),kw_data["slug"])
    print()

    support={"sitemap.xml":build_sitemap(),"robots.txt":build_robots(),
              "llms.txt":build_llms(),"_config.yml":"# GitHub Pages\nexclude: [build.py]\n"}
    with open(DIST+"/.nojekyll","w") as f: f.write("")
    with open(DIST+"/.github/workflows/deploy.yml","w") as f: f.write(WORKFLOW)
    print("\n  Support files:")
    for fname,content in support.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(content)
        print(f"    ✓ {fname}")
    print("    ✓ .nojekyll  ✓ .github/workflows/deploy.yml")

    total_sz=sum(os.path.getsize(os.path.join(r,fn)) for r,_,files in os.walk(DIST) for fn in files)
    total_files=sum(len(files) for _,_,files in os.walk(DIST))
    report={"build_date":BUILD_DATE,"domain":SITE_DOMAIN,"keyword_pages":len(KEYWORDS),
             "blog_posts":len(BLOG_POSTS),"total_files":total_files,
             "total_size_mb":round(total_sz/1024/1024,2),"affiliate_url":AFFILIATE_URL}
    with open(DIST+"/build-report.json","w") as f: json.dump(report,f,indent=2)
    print("    ✓ build-report.json")

    print(f"""
{'═'*60}
  ✅  BUILD COMPLETE
{'═'*60}
  Keyword pages:    {len(KEYWORDS):>5}
  Blog posts:       {len(BLOG_POSTS):>5}
  Essential pages:  {len(essential):>5}
  Total files:      {total_files:>5}
  Sitemap URLs:     {len(KEYWORDS)+len(BLOG_POSTS)+10:>5}
  Total size:       {round(total_sz/1024/1024,1):>4.1f} MB
  Output:           ./dist/
{'═'*60}

  Repo: https://github.com/brightlane/pixcutsonline
  Live: {SITE_DOMAIN}/
""")

if __name__=="__main__":
    main()
