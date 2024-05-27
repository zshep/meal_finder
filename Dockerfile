FROM python:3.10

WORKDIR app/


COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "app.py", "run"  ]

