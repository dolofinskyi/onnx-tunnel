from fastapi import FastAPI


def create_app(args) -> FastAPI:
    from .routers import index_router 
    from .lifespan import create_lifespan

    lifespan = create_lifespan(args)


    app = FastAPI(lifespan=lifespan)


    app.include_router(index_router)


    return app