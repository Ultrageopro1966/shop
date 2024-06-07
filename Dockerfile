# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-buster

# Install pip requirements
RUN pip install poetry

# Copy local code to the container image.
COPY . .

# Install production dependencies.
RUN poetry install

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app" ]
