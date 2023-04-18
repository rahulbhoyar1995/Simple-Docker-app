# Simple-Docker-app

This is a simple Docker application in Python that demonstrates how to containerize a Python script.

### Author 

Rahul Bhoyar

### Getting Started

To get started with this project, you will need to have Docker installed on your system. If you don't have Docker installed, you can download and install it from the [Docker website](https://www.docker.com/get-started).

### Building the Docker Image

To build the Docker image, navigate to the root of the project directory and run the following command:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>perl</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-perl">docker build -t my-python-app .
</code></div></div></pre>

This will build a Docker image named `my-python-app` using the Dockerfile in the project directory.

### Running the Docker Container

To run the Docker container, use the following command:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>arduino</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-arduino">docker run my-python-app
</code></div></div></pre>

This will start a container using the `my-python-app` image and run the Python script inside the container.

## Customizing the Python Script

To customize the Python script, edit the `main.py` file in the project directory. Once you have made your changes, rebuild the Docker image using the `docker build` command.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to submit a pull request or create an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
