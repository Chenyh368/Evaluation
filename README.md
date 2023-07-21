# Object Detection Evaluation
- This code is heavily based on https://github.com/rafaelpadilla/Object-Detection-Metrics. You can refer it to get more details.
## Quick start

### Create the ground truth files
- To evaluate your model, please first create ground truth text file for each image. You can look up sample_1 in data folder to get the example. Each line in your label file should be:
`<class_name> <left> <top> <right> <bottom>`
- E.g. The ground truth bounding boxes of the image "2008_000034.jpg" are represented in the file "2008_000034.txt":
  ```
  bottle 6 234 45 362
  person 1 156 103 336
  person 36 111 198 416
  person 91 42 338 500
  ```
- The script that read xml file in PascalVOC format to a dict is in notebook read_plot_gt.ipynb.
### Create your detection files
- Create a separate detection text file for each image in the folder.
- The names of the detection files must match their correspond ground truth (e.g. "detections/2008_000182.txt" represents the detections of the ground truth: "groundtruths/2008_000182.txt").
- In these files each line should be in the following format: `<class_name> <confidence> <left> <top> <right> <bottom>`
- E.g. "2008_000034.txt":
    ```
    bottle 0.14981 80 1 295 500  
    bus 0.12601 36 13 404 316  
    horse 0.12526 430 117 500 307  
    pottedplant 0.14585 212 78 292 118  
    tvmonitor 0.070565 388 89 500 196  
    ```

### Run Evaluation

As you have generated all the txt files, like files in data/sample_2, you can simply run script like `python pascalvoc.py -gt ./data/sample_2/groundtruths/ -det ./data/sample_2/detections/ -t 0.3` to get the evaluation result,
or you can simply refer to `evaluate_sample_2.ipynb`.
Note that if you want to do more like using other coordinate format, please refer to https://github.com/rafaelpadilla/Object-Detection-Metrics.

### Submission
You should submit your result in the format mentioned in **Create your detection files**:
- Result should be stored in a **single** text file for every image.
- In these files each line should be in the following format: `<class_name> <confidence> <left> <top> <right> <bottom>`
- Then you should compress them in a single ZIP file and then submit. The name of the compressed file should be `submission_YOURTEAMNAME`.
- For example, if the number of your team name is `MYTEAM`, and the test data contains three images: `01.jpg, 02.jpg, 03.jpg`, your submission
should be `submission_MYTEAM.zip` with three text files `01.txt` `02.txt` `03.txt` inside. Each one contains the prediction results of the corresponding image.