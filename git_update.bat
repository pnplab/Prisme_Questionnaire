@echo OFF
rem Activate conda environment for prisme project.
call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\Users\PnPLab\.conda\envs\prisme

rem Run git update then push
CD C:\Users\PnPLab\Desktop\Prisme\Prisme_Questionnaire
call git status
call git add *
call git commit -am "auo-update from prisme laptop"
call git push

rem Deactivate the environment
call conda deactivate

rem If conda is directly available from the command line then the following code works.
rem call activate someenv
rem python script.py
rem conda deactivate
PAUSE
rem One could also use the conda run command
rem conda run -n someenv python script.py