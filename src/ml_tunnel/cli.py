import argparse
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        prog="ml-tunnel",
        description="FastAPI server for ONNX models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
                Usage examples:
                %(prog)s --model model.onnx
                %(prog)s --model model.onnx --port 8080 --host 127.0.0.1
            """
    )

    parser.add_argument(
        "--model", 
        type=str,
        required=True,
        help="Path to .onnx model (required)"
    )

    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host for server (default: 127.0.0.1)"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for server (default: 8000)"
    )

    return parser.parse_args()

def validate_args(args):
    if not os.path.exists(args.model):
        print(f"Error: Model not found: {args.model}")
        return False
    
    if not args.model.lower().endswith('.onnx'):
        print(f"Models extension must be .onnx: {args.model}")
        return False
    
    if args.port < 1 or args.port > 65535:
        print(f"invalid port: {args.port}")
        return False
    
    return True


def main():
    try:
        args = parse_args()
        
        if not validate_args(args):
            sys.exit(1)
        
        import uvicorn
        from .server import app
        
        uvicorn.run(
            app,
            host=args.host,
            port=args.port,
        )
        
    except KeyboardInterrupt:
        print("Server was stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Exception: {e}")
        sys.exit(1)