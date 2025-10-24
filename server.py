#!/usr/bin/env python3
"""
Simple HTTP server to serve the One Task app.
This avoids CORS issues that occur when opening the HTML file directly.

Usage:
    python3 server.py

Then open: http://localhost:8000
"""

import http.server
import socketserver
import os

PORT = 8000

# Change to the directory where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow Google Sheets requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom log format
        print(f"[Server] {args[0]}")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"✓ Server running at http://localhost:{PORT}")
        print(f"✓ Open your browser to: http://localhost:{PORT}")
        print(f"✓ Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✓ Server stopped")
