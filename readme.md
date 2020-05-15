# Full Stack Deep Learning Labs

Welcome!

Project developed during lab sessions of the [Full Stack Deep Learning Bootcamp](https://fullstackdeeplearning.com).

- We will build a handwriting recognition system from scratch, and deploy it as a web service.
- Uses Keras, but designed to be modular, hackable, and scalable
- Provides code for training models in parallel and store evaluation in Weights & Biases
- We will set up continuous integration system for our codebase, which will check functionality of code and evaluate the model about to be deployed.
- We will package up the prediction system as a REST API, deployable as a Docker container.
- We will deploy the prediction system as a serverless function to Amazon Lambda.
- Lastly, we will set up monitoring that alerts us when the incoming data distribution changes.

## Schedule for the Spring 2019 Bootcamp

- First session (90 min)
  - Overview of the labs. (15 min)
  - Get set up. (10 min)
  - Lab 1 (20 min): Project structure. 
  - Lab 2 (25 min): Introduce EMNIST. Training code details. Train & evaluate character prediction baselines.
  - Lab 3 (20 min): Introduce EMNIST Lines. Overview of model architecture. Train our model on EMNIST Lines.
- Second session (60 min)
  - Lab 4 (20 min): Weights & Biases + parallel experiments.
  - Lab 5 (40 min): IAM Lines and experimentation time (launch a bunch of experiments, leave running overnight in a shared W&B).
- Third session (90 min)
  - Review results from the class on W&B
  - Lab 6 (60 min) line detection task
  - Lab 7 (30 min) data labeling
    - Go through data versioning and even have a little labeling interface for fresh data that they generated on the first day
- Fourth session (75 min)
  - Lab 8 (15 min) continuous integration
  - Lab 8 (60 min) web deployment

# Setup


## 1. Set up your machine

- In the live class we used a sponsored instance of Jupyter Hub to run experiments. 
- You can use Google Colab to run your projects on a notebook in the cloud.
- We recommend Weights & Biases for experiment tracking. It's a free tool for students, and you can learn more at wandb.com.


## 2. Check out the repo

You should already have the repo in your home directory. Go into it and make sure you have the latest.

```sh
cd fsdl-text-recognizer-project
git pull origin master
```

If not, open a shell in your JupyterLab instance and run

```sh
git clone https://github.com/gradescope/fsdl-text-recognizer-project.git
cd fsdl-text-recognizer-project
```


## 3. Set up the Python environment

1. Direct to the project root folder
2. Run `pipenv install --dev` to install both dependencies and dev-dependencies(Note: In this project, we use `python3.7`, since python version in Google AI Platform Notebooks is `3.7`)
3. Run `sh setup.sh`
4. From now on, precede commands with `pipenv run` to make sure they use the correct environment.(Note: If there is `module not found error`, run `sh setup_python.sh` first)

# Ready

Now you should be setup for the labs. The instructions for each lab are in readme files in their folders.

You will notice that there are solutions for all the labs right here in the repo, too.
If you get stuck, you are welcome to take a look!
