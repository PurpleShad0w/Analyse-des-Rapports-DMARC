from grafanalib.core import Dashboard
from grafanalib._gen import DashboardEncoder
from grafana_client import GrafanaApi
from grafana_client.util import setup_logging
from typing import Dict
import json
import logging

logger = logging.getLogger(__name__)

with open('data/Grafana-DMARC_Reports.json', 'r', encoding='utf-8') as f:
    template = json.loads(f.read())
    use_template = True

dashboard = Dashboard(
    title="DMARC Analysis Report",
    description="Summary of the data obtained via analysis of the provided DMARC reports",
    tags=['dmarc'],
    timezone="browser",
    panels=[],
).auto_panel_ids()

def mkdashboard(message: str = None, overwrite: bool = False) -> Dict:
    data = {
        "dashboard": encode_dashboard(dashboard),
        "overwrite": overwrite,
        "message": message,
    }
    return data

def encode_dashboard(entity) -> Dict:
    if use_template:
        return template

    return json.loads(json.dumps(entity, sort_keys=True, cls=DashboardEncoder))

def run(grafana: GrafanaApi):
    dashboard_payload = mkdashboard(
        message="Updated by grafanalib",
        overwrite=True)

    response = grafana.dashboard.update_dashboard(dashboard_payload)
    print(json.dumps(response, indent=2))

if __name__ == "__main__":

    setup_logging(level=logging.DEBUG)
    grafana_client = GrafanaApi.from_url()
    run(grafana_client)