# ML-end-to-end-Taxi-Demand-Prediction-in-Chicago
End to End Taxi Demand Prediction Machine Learning Model using Visual studio, Github actions, Flask, Heroku, and Dockers

> Final output website link - https://taxi-demand-prediction-chicago-3848f310efca.herokuapp.com/

> Step 1: Cloning the Git repository
>    - Open command prompt and change the drive you need for cloning, Say E:, by typing <E:>
>    - Change the path to exact folder by typing <cd E:/file/path>
>    - Copy the web URL of the git and Clone using the command <git clone <web url for cloning>> 

> Step 2: Paste the code and the pickle files of the model and any preprocessing steps

> Step 3: Setup a new environment
>   - Open command prompt terminal on visual studio and use the command <conda create -p venv python==3.9 -y>
>   - Activate the environment with the command <conda activate E:/file/path>

> Step 4: Install relevant libraries
>   - Create requirements.txt file, add the relevant libraries such as scikit-learn, numpy, seaborn etc.
>   - Install by running the following command in the cmd terminal of visual studio <pip install -r requirements.txt>

> Step 4: Pushing the code and pickle files to the Github repository
>   - Configure github using <git config --global user.name "any user name">
>   - Followed by <git config --global user.email "email_id_used_for_github">
>   - Add files <git add "file.format">
>   - To add all files <git add .>
>   - Commit <git commit -m "any message">
>   - Push <git push origin main>
>   - If for some reason, you want to delete all previous commits <git reset --hard HEAD^> # be careful with this, it may clean up entire repository
>   - Better delete last n previous commits that you don't want <git reset --hard HEAD~2> # to delete last 2 commits. But after the resetting step, push the new changes using <git push origin main --force>
>

> Step 5: Create app.py and include the Flask code to retrieve features and perform model prediction

> Step 6: Run the app.py file using <python app.py>


