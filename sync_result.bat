@echo OFF
rem How to run a Python scripts in a given conda environment from a batch file.

call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\Users\PnPLab\.conda\envs\prisme

rem Run a result sync to elm remote server in that environment
CD \Users\PnPLab\Desktop\Prisme\Prisme_Questionnaire\result
scp -r *.csv elm:/data/orban/data/prisme_questions/result/.
rem Run a backup also on elm
CD \Users\PnPLab\Desktop\Prisme\Prisme_Questionnaire\
restic -r sftp:elm:/data/orban/data/prisme_questions/restic-repo --verbose backup result

PAUSE
rem Deactivate the environment
call conda deactivate
