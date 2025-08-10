# Static Assets

Frontend assets including CSS, JavaScript, and images.

## Structure:
- `css/tailwind.css` - Compiled Tailwind CSS framework
- `css/custom.css` - Custom styles and template-specific overrides
- `js/alpine.min.js` - Alpine.js for reactive components
- `js/app.js` - Custom JavaScript for form handling and interactions
- `images/template_previews/` - Preview images for template selection
- `images/branding/` - Logo, favicon, and brand assets

## Build Process:
- Tailwind CSS compilation with purging for production
- JavaScript minification and bundling
- Image optimization and responsive variants
- CDN deployment via Cloudflare

## Performance:
- Lazy loading for images
- CSS/JS compression
- Browser caching headers
- WebP image format support