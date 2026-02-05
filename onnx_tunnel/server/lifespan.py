from contextlib import asynccontextmanager

from fastapi import FastAPI

from ..registry import ModelRegistry, PipelineRegistry

def create_lifespan(args):

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.model = ModelRegistry.create(args.backend, model_path=args.model_path)
        app.state.pipeline = PipelineRegistry.create(args.backend)
        yield
    
    return lifespan