# super_teaching

### **Technologies/Frameworks/Libs used:**

- Django
- Django Rest Framework
- sqlite3 - database
- Django ORM

### Step one
#### create a virtual environment
Create and start a virtual env for the project. 

- To create the virtual environment, run:
```bash
python3 -m venv env
```
- To activate the virtual environment run:

    Linux:
    ```bash
    source env/bin/activate
    ```
    Windows:
    ```shell
    env\Scripts\activate.bat
    ```

### Step two
#### Installation of dependencies
1. __Install the packages in the virtual environment from the following command:__
    
    ```bash
    pip install -r requirements.txt
    ```

### Step three
#### Run project

1. To start the django server you need to be at the project root in the terminal and run the following command
 ~~~
    - python manage.py migrate
    - python manage.py runserver
 ~~~

Or you can run the docker commands bellow:

~~~
    - docker build -t {CONTAINER NAME} .
    - docker run -p {PORT}:{PORT} {CONTAINER NAME}}
 ~~~

2. You can change the HOST and PORT as you wish in dockerfile.

## **-- Endpoints:**

#### **Request Router:**
~~~
{HOST}/api/exercise
~~~

### EXERCISE ENDPOINTS

> _Endpoints available to get all, get by id, post and delete exercises_

- {HOST}/api/exercise - METHOD POST. Below you can find the model of body

```
{
    "exercise": 2,
    "answer": "D"
}
```

- {HOST}/api/exercise - METHOD GET
- {HOST}/api/exercise/{exercise_id} - METHOD GET (BY ID)
- {HOST}/api/exercise/{exercise_id} - METHOD DELETE


#### **Request on Router:**
~~~
{HOST}/api/answer
~~~

### ANSWER ENDPOINTS

> _Endpoints available to get all, get by id, post and delete answers_

- {HOST}/api/answer - METHOD POST. Below you can find the model of body

```
{
    "question": "As palavras que, na sequência, recebem acento gráfico são:",
    "first_alternative": "hifens – latex – avaro",
    "second_alternative": "gratuito – video – recem",
    "third_alternative": "benção – egoista – vies",
    "fourth_alternative": "martir – item – economia",
    "fifth_alternative": "caracteres – seca – rubrica",
    "answer": "C"
}
```

- {HOST}/api/answer - METHOD GET
- {HOST}/api/answer/{answer_id} - METHOD GET (BY ID)
- {HOST}/api/answer/{answer_id} - METHOD DELETE

## RESPONSES

#### **response for router {HOST}/api/exercise:**

- Here you can find all the exercises, the total exercises, the status, and the performance data.

```json
{
    "STATUS": "SUCCESS",
    "TOTAL EXERCISES": 10,
    "PERFORMANCE": {
        "total_questions": 10,
        "total_answered": 2,
        "correct_answers": 1,
        "incorrect_answers": 1,
        "performance_percentual": "10.0%"
    },
    "EXERCISES": [
        {
            "id": 1,
            "question": "Em relação ao número de sílabas e sua classificação especificados entre parênteses, assinale a alternativa incorreta.",
            "first_alternative": "BRINQUEDOS - TRISSILABA",
            "second_alternative": "ARRUMA - POLISSILABA",
            "third_alternative": "NÃO - MONOSSILABA",
            "fourth_alternative": "NADA - DISSILABA",
            "fifth_alternative": "",
            "answer": "D",
            "question_answered": [
                {
                    "id": 1,
                    "answer": "D",
                    "is_answered": true
                }
            ]
        },
        {
            "id": 2,
            "question": "Ache a palavra com erro de grafia",
            "first_alternative": "cabeleireiro ; manteigueira",
            "second_alternative": "caranguejo ; beneficência",
            "third_alternative": "prazeirosamente ; adivinhar",
            "fourth_alternative": "perturbar ; concupiscência",
            "fifth_alternative": "berinjela ; meritíssimo",
            "answer": "E",
            "question_answered": [
                {
                    "id": 2,
                    "answer": "D",
                    "is_answered": true
                },
                {
                    "id": 3,
                    "answer": "D",
                    "is_answered": true
                }
            ]
        },
        {
            "id": 3,
            "question": "Assinale a frase em que não há erro na forma verbal:",
            "first_alternative": "Não semeiemos a discórdia.",
            "second_alternative": "Ainda bem que freiamos a tempo.",
            "third_alternative": "Discirno muito bem uma jóia verdadeira.",
            "fourth_alternative": "Eles se desaviram por um motivo tolo",
            "fifth_alternative": "Não demula esta parede.",
            "answer": "B",
            "question_answered": []
        }
    ]
}
```

#### Response for router {ROUTER}/api/exercise/1:

- Here you can find the answer with id 1 and linked with the Exercise detail.

```json
{
    "STATUS": "SUCCESS",
    "DATA": {
        "EXERCISE DETAILS": {
            "id": 1,
            "question": "Em relação ao número de sílabas e sua classificação especificados entre parênteses, assinale a alternativa incorreta.",
            "first_alternative": "BRINQUEDOS - TRISSILABA",
            "second_alternative": "ARRUMA - POLISSILABA",
            "third_alternative": "NÃO - MONOSSILABA",
            "fourth_alternative": "NADA - DISSILABA",
            "fifth_alternative": "",
            "answer": "D",
            "question_answered": [
                {
                    "id": 1,
                    "answer": "D",
                    "is_answered": true
                }
            ]
        }
    }
}
```

#### Response for router {ROUTER}/api/answer:

- Here you can find all the answers.

```json
{
    "STATUS": "SUCCESS",
    "TOTAL ANSWERS": 3,
    "ANSWERS": [
        {
            "id": 1,
            "answer": "D",
            "is_answered": true,
            "exercise": 1
        },
        {
            "id": 2,
            "answer": "D",
            "is_answered": true,
            "exercise": 2
        },
        {
            "id": 3,
            "answer": "D",
            "is_answered": true,
            "exercise": 2
        }
    ]
}
```

## UNIT TESTS

- On your command line at the root project, run the command: `./manage.py test`
