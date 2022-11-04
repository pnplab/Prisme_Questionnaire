@echo OFF
rem Activate conda environment for prisme projet.
call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\Users\PnPLab\.conda\envs\prisme

rem Run a backup of result flder to elm remote server
CD \Users\PnPLab\result
scp -r *.csv elm:/data/orban/data/prisme_questions/result/.
rem Run an encripted backup also on elm, the password is 'prisme'.
CD \Users\PnPLab
restic -r sftp:elm:/data/orban/data/prisme_questions/restic-repo --verbose backup result

PAUSE
rem Deactivate the environment
call conda deactivate
