# UIT Portal Feedback Automation

Every year, UIT students are asked to submit lengthy and repetitive faculty feedback forms multiple times. I wrote this script to automate that process. It will submit all the feedback forms for you!

## Prerequisites

1. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Navigate to the `src` directory**:

   ```bash
   cd src
   ```

3. **Update the .env file in the src directory with your UIT portal credentials. You only need to set your username (UIT_PORTAL_USERNAME) and password (UIT_PORTAL_PASSWORD). Leave the URL as it is, unless it changes (it might change in the future, idk)**:

   ```
   UIT_PORTAL_URL=https://eduboard.uit.edu/StudentPortal/Login
   UIT_PORTAL_USERNAME=SET_YOUR_USERNAME
   UIT_PORTAL_PASSWORD=SET_YOUR_PASSWORD
   ```

## Usage

After setting up the environment, simply run the script:

```bash
python app.py
```

The script will open a browser, log in to the UIT portal, and complete the feedback submission automatically. Enjoy!
