#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# Standard libraries.
import sys
from pathlib import Path

# Vendor libraries.
from appcli.cli_builder import create_cli
from appcli.models.configuration import Configuration
from appcli.orchestrators import DockerComposeOrchestrator

# ------------------------------------------------------------------------------
# CONSTANTS
# ------------------------------------------------------------------------------

# directory containing this script
BASE_DIR = Path(__file__).parent

# ------------------------------------------------------------------------------
# PRIVATE METHODS
# ------------------------------------------------------------------------------

def main():
    configuration = Configuration(
        app_name='myapp',
        docker_image='brightsparklabs/myapp',
        seed_app_configuration_file=BASE_DIR / 'resources/settings.yml',
        application_context_files_dir=BASE_DIR / 'resources/templates/appcli/context',
        stack_configuration_file=BASE_DIR / 'resources/stack-settings.yml',
        baseline_templates_dir=BASE_DIR / 'resources/templates/baseline',
        configurable_templates_dir=BASE_DIR / 'resources/templates/configurable',
        orchestrator=DockerComposeOrchestrator(
            # NOTE: These paths are relative to 'resources/templates/baseline'.
            docker_compose_file = Path('docker-compose.yml')
        ),
    )
    cli = create_cli(configuration)
    cli()

# ------------------------------------------------------------------------------
# ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

