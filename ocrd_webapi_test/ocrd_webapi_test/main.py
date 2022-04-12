from fastapi import FastAPI
import datetime
import os
import psutil
from typing import List

from .models import (
    DiscoveryResponse,
    Workspace,
)

app = FastAPI(
    title='OCR-D Web API',
    description='HTTP API for offering OCR-D processing',
    contact={'email': 'test@example.com'},  # TODO: update if needed
    license={
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
    version='0.0.1',
    servers=[
        {
            'url': 'https://example.org/ocrd/v1',  # TODO: update if needed
            'description': 'The URL of your server offering the OCR-D API.',
        }
    ],
)


@app.get('/')
async def test():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


@app.get('/discovery', response_model=DiscoveryResponse)
async def discovery() -> DiscoveryResponse:
    # TODO: fill response with content
    res = DiscoveryResponse()
    res.ram = psutil.virtual_memory().total / (1024.**3)
    res.cpu_cores = os.cpu_count()
    res.has_cuda = False
    res.has_ocrd_all = False
    res.has_docker = False
    return res


@app.get('/workspace', response_model=List[Workspace])
def get_workspaces() -> List[Workspace]:
    pass


@app.post('/workspace', response_model=None, responses={'201': {'model': Workspace}})
def create_workspace() -> None | Workspace:
    """
    Post a new workspace
    """
    return Workspace(id="dummyId", description="dummyDesc")
