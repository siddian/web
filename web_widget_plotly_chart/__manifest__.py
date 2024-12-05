{
    "name": "Web Widget Plotly",
    "summary": """Allow to draw plotly charts.""",
    "author": "LevelPrime srl, Odoo Community Association (OCA)",
    "maintainers": ["robyf70"],
    "website": "https://github.com/OCA/web",
    "category": "Web",
    "version": "15.0.1.0.0",
    "depends": ["web"],
    "data": [],
    "external_dependencies": {
        "python": ["plotly==5.13.1"],
    },
    "license": "LGPL-3",
    "assets": {
        "web.assets_backend": [
            "web_widget_plotly_chart/static/src/js/widget_plotly.esm.js",
        ],
    },
}
