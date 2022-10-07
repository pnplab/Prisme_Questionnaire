@echo OFF
rem Run Python scripts in a given conda environment from a batch file.

call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\Users\PnPLab\.conda\envs\prisme

rem Run a python script in that environment
CD C:\Users\PnPLab\Desktop\Prisme\Prisme_Questionnaire
call python C:\Users\PnPLab\Desktop\Prisme\Prisme_Questionnaire\Questionnaire_autorapporte_evaluation.py

rem Deactivate the environment
call conda deactivate

rem If conda is directly available from the command line then the following code works.
rem call conda activate someenv
rem python script.py
rem conda deactivate

rem One could also use the conda run command
rem conda run -n someenv python script.py