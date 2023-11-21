from pension_project.wsgi import application

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    # Additional Gunicorn configuration for serving static files
    from django.core.management import call_command
    call_command('collectstatic', interactive=False, clear=True)