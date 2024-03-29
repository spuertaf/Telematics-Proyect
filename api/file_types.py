import os

def getContentType(new_path):
    
    extensions = {
        '.3gp': 'video/3gpp',
        '.7z': 'application/x-7z-compressed',
        '.aac': 'audio/aac',
        '.abw': 'application/x-abiword',
        '.arc': 'application/x-freearc',
        '.avi': 'video/x-msvideo',
        '.azw': 'application/vnd.amazon.ebook',
        '.bin': 'application/octet-stream',
        '.bmp': 'image/bmp',
        '.bz': 'application/x-bzip',
        '.bz2': 'application/x-bzip2',
        '.csh': 'application/x-csh',
        '.css': 'text/css',
        '.csv': 'text/csv',
        '.doc': 'application/msword',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.eot': 'application/vnd.ms-fontobject',
        '.epub': 'application/epub+zip',
        '.gif': 'image/gif',
        '.htm': 'text/html',
        '.html': 'text/html',
        '.ico': 'image/vnd.microsoft.icon',
        '.ics': 'text/calendar',
        '.jar': 'application/java-archive',
        '.jpeg': 'image/jpeg',
        '.jpg': 'image/jpeg',
        '.js': 'text/javascript',
        '.json': 'application/json',
        '.jsonld': 'application/ld+json',
        '.mid': 'audio/midi',
        '.midi': 'audio/midi',
        '.mjs': 'text/javascript',
        '.mp3': 'audio/mpeg',
        '.mpeg': 'video/mpeg',
        '.mpkg': 'application/vnd.apple.installer+xml',
        '.m4a': 'audio/mp4',
        '.m4b': 'audio/mp4',
        '.odp': 'application/vnd.oasis.opendocument.presentation',
        '.ods': 'application/vnd.oasis.opendocument.spreadsheet',
        '.odt': 'application/vnd.oasis.opendocument.text',
        '.oga': 'audio/ogg',
        '.ogv': 'video/ogg',
        '.ogx': 'application/ogg',
        '.opus': 'audio/opus',
        '.otf': 'font/otf',
        '.pdf': 'application/pdf',
        '.php': 'application/x-httpd-php',
        '.png': 'image/png',
        '.ppt': 'application/vnd.ms-powerpoint',
        '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        '.rar': 'application/x-rar-compressed',
        '.rtf': 'application/rtf',
        '.sh': 'application/x-sh',
        '.svg': 'image/svg+xml',
        '.swf': 'application/x-shockwave-flash',
        '.tar': 'application/x-tar',
        '.tif': 'image/tiff',
        '.tiff': 'image/tiff',
        '.ts': 'video/mp2t',
        '.ttf': 'font/ttf',
        '.txt': 'text/plain',
        '.wav': 'audio/wav',
        '.webm': 'video/webm',
        '.webp': 'image/webp',
        '.wma': 'audio/x-ms-wma',
        '.wmv': 'video/x-ms-wmv',
        '.woff': 'font/woff',
        '.woff2': 'font/woff2',
        '.xhtml': 'application/xhtml+xml',
        '.xls': 'application/vnd.ms-excel',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        '.xml': 'application/xml',
        '.xpm': 'image/x-xpixmap',
        '.xwd': 'image/x-xwindowdump',
        '.yaml': 'text/yaml',
        '.yml': 'text/yaml',
        '.zip': 'application/zip',
        '.html': 'text/html',
        '.xml': 'application/xml',
        '.pdf': 'application/pdf',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.bmp': 'image/bmp',
        '.ico': 'image/x-icon',
        '.svg': 'image/svg+xml',
        '.tif': 'image/tiff',
        '.tiff': 'image/tiff',
        '.wav': 'audio/wav',
        '.mp3': 'audio/mpeg',
        '.ogg': 'audio/ogg',
        '.mid': 'audio/midi',
        '.midi': 'audio/midi',
        '.mp4': 'video/mp4',
        '.avi': 'video/x-msvideo',
        '.wmv': 'video/x-ms-wmv',
        '.mkv': 'video/x-matroska',
        '.txt': 'text/plain',
        '.csv': 'text/csv',
        '.tsv': 'text/tab-separated-values',
        '.doc': 'application/msword',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.xls': 'application/vnd.ms-excel',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        '.ppt': 'application/vnd.ms-powerpoint',
        '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        '.zip': 'application/zip',
        '.tar': 'application/x-tar',
        '.gz': 'application/gzip',
        '.rar': 'application/x-rar-compressed',
        '.7z': 'application/x-7z-compressed',
        '.exe': 'application/x-msdownload',
        '.dll': 'application/x-msdownload',
        '.py': 'text/x-python',
        '.cpp': 'text/x-c++src',
        '.c': 'text/x-csrc',
        '.java': 'text/x-java',
        '.php': 'application/x-httpd-php',
        '.rb': 'application/x-ruby',
        '.pl': 'application/x-perl',
        '.psd': 'image/vnd.adobe.photoshop',
        '.ai': 'application/postscript',
        '.eps': 'application/postscript',
        '.indd': 'application/x-indesign',
        '.cdr': 'application/cdr',
        '.dwg': 'application/acad',
        '.dxf': 'application/dxf',
        '.3gp': 'video/3gpp',
        '.3g2': 'video/3gpp2',
        '.asf': 'video/x-ms-asf',
        '.asx': 'video/x-ms-asf',
        '.flv': 'video/x-flv',
        '.m3u': 'audio/x-mpegurl',
        '.m4a': 'audio/mp4a-latm',
        '.m4v': 'video/x-m4v',
        '.mov': 'video/quicktime',
        '.mpa': 'audio/mpeg',
        '.mpe': 'video/mpeg',
        '.mpeg': 'video/mpeg',
        '.mpg': 'video/mpeg',
        '.ogg': 'application/ogg',
        '.rm': 'application/vnd.rn-realmedia',
        '.swf': 'application/x-shockwave-flash',
        '.wmf': 'image/wmf',
        '.svgz': 'image/svg+xml',
        '.mht': 'message/rfc822',
        '.mhtml': 'message/rfc822',
        '.eml': 'message/rfc822',
        '.ics': 'text/calendar',
        '.jar': 'application/java-archive',
        '.war': 'application/java-archive',
        '.ear': 'application/java-archive',
        '.rtf': 'application/rtf',
        '.apk': 'application/vnd.android.package-archive',
        '.db': 'application/x-sqlite3',
        '.sqlite': 'application/x-sqlite3',
        '.sql': 'application/sql',
        '.cab': 'application/vnd.ms-cab-compressed',
        '.deb': 'application/x-debian-package',
        '.rpm': 'application/x-redhat-package-manager',
        '.xml.gz': 'application/gzip',
        '.tar.gz': 'application/gzip',
        '.sql.gz': 'application/gzip',
        '.html.gz': 'application/gzip',
        '.css.gz': 'application/gzip',
        '.js.gz': 'application/gzip',
        '.json.gz': 'application/gzip',
        '.txt.gz': 'application/gzip',
        '.csv.gz': 'application/gzip',
        '.tsv.gz': 'application/gzip',
        '.pdf.gz': 'application/gzip',
        '.log': 'text/plain',
        '.md': 'text/markdown',
        '.yml': 'text/yaml',
        '.yaml': 'text/yaml',
        '.ini': 'text/x-ini',
        '.conf': 'text/x-conf',
        '.sh': 'application/x-sh',
        '.bash': 'application/x-sh',
        '.zsh': 'application/x-sh',
        '.fish': 'application/x-fish',
        '.ksh': 'application/x-ksh',
        '.csh': 'application/x-csh',
        '.odt': 'application/vnd.oasis.opendocument.text',
        '.ott': 'application/vnd.oasis.opendocument.text-template',
        '.odm': 'application/vnd.oasis.opendocument.text-master',
        '.odg': 'application/vnd.oasis.opendocument.graphics',
        '.otg': 'application/vnd.oasis.opendocument.graphics-template',
        '.odp': 'application/vnd.oasis.opendocument.presentation',
        '.otp': 'application/vnd.oasis.opendocument.presentation-template',
        '.ods': 'application/vnd.oasis.opendocument.spreadsheet',
        '.ots': 'application/vnd.oasis.opendocument.spreadsheet-template',
        '.odc': 'application/vnd.oasis.opendocument.chart',
        '.odf': 'application/vnd.oasis.opendocument.formula',
        '.odb': 'application/vnd.oasis.opendocument.database',
        '.odft': 'application/vnd.oasis.opendocument.formula-template',
        '.odp': 'application/vnd.oasis.opendocument.presentation',
        '.pptm': 'application/vnd.ms-powerpoint.presentation.macroEnabled.12',
        '.potm': 'application/vnd.ms-powerpoint.template.macroEnabled.12',
        '.ppam': 'application/vnd.ms-powerpoint.addin.macroEnabled.12',
        '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        '.potx': 'application/vnd.openxmlformats-officedocument.presentationml.template',
        '.ppsx': 'application/vnd.openxmlformats-officedocument.presentationml.slideshow'
    }
    extension = os.path.splitext(new_path)[1]
    content_type = extensions.get(extension, 'application/octet-stream')
    return content_type