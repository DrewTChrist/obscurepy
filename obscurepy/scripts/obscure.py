from obscurepy.obfuscator import Obfuscator
import click


@click.command()
@click.option('--filepath', help='File path to provide if you would like to obscure a single file')
@click.option('--project_dir', help='The directory of the project to obscure')
@click.option('--output_dir', default='.', help='The directory to output the obscured code')
@click.option('-l', '--log', is_flag=True, default=False, help='Enable this flag to turn on logging')
@click.option('-p', '--plugins', is_flag=True, default=False, help='Enable this flag if you wish to load your own '
                                                                   'handlers')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Enable this flag to write logging to stdout')
def obscure(filepath, plugins, project_dir, output_dir, log, verbose):
    """Make your Python code difficult to read"""
    check_bad_option_usage(filepath, plugins, project_dir, output_dir)
    Obfuscator(filepath, plugins, project_dir,
               output_dir, log, verbose).obscure()


def check_bad_option_usage(filepath, plugins, project_dir, output_dir):
    """Validates the arguments passed to the Obfuscator"""
    if filepath and project_dir:
        raise click.BadOptionUsage('project_dir',
                                   'You cannot provide a filepath and a project directory')
    elif not filepath and not project_dir and (output_dir == '.'):
        raise click.MissingParameter(
            'You must provide some arguments to obscure')
