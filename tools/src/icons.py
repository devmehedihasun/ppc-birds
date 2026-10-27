# Inline SVG icon set (24x24, stroke). Usage: icon('search')
_P = {
 'search':  '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.7-3.7"/>',
 'chat':    '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4L3 21l1.1-8.8A8.4 8.4 0 1 1 21 11.5z"/>',
 'bars':    '<path d="M3 20V10m6 10V4m6 16v-7m6 7V8"/>',
 'trend':   '<path d="M3 15l5-5 4 3 8-8"/><path d="M15 5h5v5"/>',
 'phone':   '<path d="M21.5 16.9v2.6a2 2 0 0 1-2.2 2 19.6 19.6 0 0 1-8.5-3 19.3 19.3 0 0 1-6-6 19.6 19.6 0 0 1-3-8.6A2 2 0 0 1 3.8 1.7h2.6a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L7.5 9.6a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.9.7a2 2 0 0 1 1.8 2.1z"/>',
 'layout':  '<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 9h18M9 21V9"/>',
 'browser': '<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M3 9h18M6.6 6.5h.01M9.6 6.5h.01"/>',
 'bag':     '<path d="M4 7h16l-1.4 12.2a2 2 0 0 1-2 1.8H7.4a2 2 0 0 1-2-1.8L4 7z"/><path d="M9 7V5.5a3 3 0 0 1 6 0V7"/>',
 'shield':  '<path d="M9 12l2 2 4-4"/><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6z"/>',
 'target':  '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
 'bolt':    '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 'users':   '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M17 11a3 3 0 1 0-1-5.8M21.5 20a5.5 5.5 0 0 0-3.5-5"/>',
 'globe':   '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 'code':    '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 4l-4 16"/>',
 'spark':   '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
 'music':   '<path d="M9 18V5l10-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="16" cy="16" r="3"/>',
 'dollar':  '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 'chart':   '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/>',
 'layers':  '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 12 10 5 10-5M2 17l10 5 10-5"/>',
 'cursor':  '<path d="m4 4 7 17 2.5-7.5L21 11z"/>',
 'gauge':   '<path d="M12 14l4-4"/><path d="M3.3 17a9 9 0 1 1 17.4 0"/>',
 'clock':   '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'mail':    '<rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
 'tag':     '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
 'server':  '<rect x="3" y="3" width="18" height="7" rx="2"/><rect x="3" y="14" width="18" height="7" rx="2"/><path d="M7 6.5h.01M7 17.5h.01"/>',
 'filter':  '<path d="M3 4h18l-7 8.5V20l-4-2v-5.5z"/>',
 'eye':     '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'heart':   '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/>',
 'home':    '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 'cross':   '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
 'leaf':    '<path d="M11 20A7 7 0 0 1 4 13c0-6 6-9 16-10-1 10-4 16-10 16"/><path d="M4 21c4-4 7-6 12-9"/>',
 'cart':    '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.6 12.4a2 2 0 0 0 2 1.6h8.8a2 2 0 0 0 2-1.6L22 7H6"/>',
 'wrench':  '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
 'pin':     '<path d="M20 10.5c0 6-8 12.5-8 12.5s-8-6.5-8-12.5a8 8 0 1 1 16 0z"/><circle cx="12" cy="10.5" r="2.8"/>',
 'check':   '<path d="m5 12.5 4.5 4.5L19 7"/>',
 'refresh': '<path d="M21 12a9 9 0 1 1-2.6-6.4L21 8"/><path d="M21 3v5h-5"/>',
 'calendar':'<rect x="3" y="4.5" width="18" height="16.5" rx="2.5"/><path d="M3 9.5h18M8 3v3M16 3v3"/>',
 'user':    '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 'folder':  '<path d="M3 6.5A1.5 1.5 0 0 1 4.5 5H9l2 2.5h8.5A1.5 1.5 0 0 1 21 9v9.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/>',
 'help':    '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"/>',
 'lock':    '<rect x="4" y="10.5" width="16" height="10.5" rx="2.5"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5"/>',
}

def icon(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')

ARROW = ('<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9 9 3M4.2 3H9v4.8" '
         'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CHEV = ('<svg viewBox="0 0 8 12" fill="none" aria-hidden="true"><path d="m2 2 4 4-4 4" stroke="currentColor" '
        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
PLUS = ('<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
        '<path d="M6 1.5v9M1.5 6h9"/></svg>')
