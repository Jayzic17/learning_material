# Uses image_name as the base image for constructing this docker image
# AS: Lets you give this image a name
FROM [image_name] AS [alias]

# Copy files from source to destination
COPY [source] [destination]
COPY requirements.txt .

# Run a Bash command
RUN [bash_command]
RUN pip install -r requirements.txt

# cd command in Bash
WORKDIR [path]

# Sets the command to be run when running a container of this image
CMD [ 'command_1', "option_1", "command_2", "option_2" ]
CMD [ "python", "app.py" ]