"""Passthrough shim for EzTransformExtension extension."""
import sys

import structlog
from meltano.edk.logging import pass_through_logging_config
from eztransformextension_ext.extension import EzTransformExtension


def pass_through_cli() -> None:
    """Pass through CLI entry point."""
    pass_through_logging_config()
    ext = EzTransformExtension()
    ext.pass_through_invoker(
        structlog.getLogger("eztransformextension_invoker"),
        *sys.argv[1:] if len(sys.argv) > 1 else []
    )
