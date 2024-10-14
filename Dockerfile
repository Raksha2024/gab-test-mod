FROM python:3.10-slim

#set the working dir
WORKDIR /app

#copy the requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Copy the app to container
COPY app.py .

#Expose port
EXPOSE 3000

#Command to run the app
CMD ["python", "app.py"]

