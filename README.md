## Prisme questionnaire
Questionnaires made for the Prisme project. 
### Install
- Create a conda envirenment, then install required packages.
`conda install --file requirements.txt`
- create static folder for offline use
`mkdir static`
- install static themes
  ```
  cd statics
  npm install survey-knockout`
  npm install survey-core
  npm install surveyjs-widgets
  cd node_modules
  download_surveyjs ./ jquery modern
  ```
- create a result folder in the root of you project
`mkdir result`

- Make restic works on windows. It's a data sync command for MS like rsync (doc: https://restic.readthedocs.io)
  - install MS powershell first
    - `winget install --id Microsoft.Powershell --source winget`
  - install scoop
    - `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
    - `irm get.scoop.sh | iex`
  - install restic
    - `scoop install restic`
  - intitiate restic and start backup
    - `restic -r sftp:elm:/data/orban/data/prisme_questions/restic-repo init`
    - `restic -r sftp:elm:/data/orban/data/prisme_questions/restic-repo --verbose backup ~/result`

