# docu-qa

### You can upload a .txt document and question it. based on openAI

## Table of Content

- [Setup](https://github.com/nur0078/docu-qa/blob/master/README.md#setup)

* [Running the App](https://github.com/nur0078/docu-qa/blob/master/README.md#running-the-app)

- [About environment variables](https://github.com/nur0078/docu-qa/blob/master/README.md#about-environment-variables)

# Setup

1.  ### install required dependencies such as flask, openai.

2.  ### Get your API key and organization ID.

    **[Your API Key](https://platform.openai.com/account/api-keys)**

    **[Org ID](https://platform.openai.com/account/api-keys)**

3.  Set environment variable

    > to do so, you will need API key and organization ID.

    open terminal in the application directory (`~/docu-qa/`) and run the following:

    `$ export OPENAI_ORGANIZATION_ID="your_org_id"`

    `$ export OPENAI_API_KEY="your_api_key"`

    **Notes:** <br />
    $ means terminal so you dont need to type that.  
    replace the "your_org_id" and "your_api_key" with your organization ID and open API key respectively.  
    Your org ID and API key should not be wrapped around quotations.

# Running the App

1.  ### open terminal in the application directory and run the app with:

    `$ python app.py`

2.  ### It automatically opens, if not, see the terminal and you should see a link similar to:

    > Running on http://127.0.0.1:5000

    use the provided link to use the app.

3.  ### Press Ctrl+C in terminal to stop the server.

# About environment variables:

- You might need to restart your IDE before you re-set environment variables.

* If you want to delete an environment variable, you can use "unset" in your terminal.  
  For example:  
  `$ unset OPENAI_API_KEY`

- if you want to print your environment variable, you can use "printenv" in your terminal.  
  For example:  
  `$ printenv OPENAI_API_KEY`
