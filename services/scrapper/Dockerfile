FROM --platform=linux/amd64 python:3.8
# Install Chrome browser and ChromeDriver dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libnss3 \
    libxi6 \
    libgconf-2-4 \
    libxcursor1 \
    libxss1 \
    libxcomposite1 \
    libasound2 \
    libxtst6 \
    xvfb

# Download and install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome-stable --version | awk -F '[ .]' '{print $3}') \
    && CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}") \
    && wget -q "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver

RUN mkdir -p /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

ENV FLASK_APP project/__init__.py
ENV APP_SETTINGS project.config.DevelopmentConfig

ENV PORT 5008

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
