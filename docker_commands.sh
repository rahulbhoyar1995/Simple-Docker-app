docker build -t rrb_python_image .

docker run -p 4000:80 rrb_python_image 