from flask import render_template


class Views:
    def index():
        return render_template('./pages/page_index.html')
