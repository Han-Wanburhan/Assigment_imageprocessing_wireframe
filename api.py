# from flask import Flask, render_template, request, jsonify
# from werkzeug.utils import secure_filename
# import os
# import subprocess
# import shutil  # Import shutil for deleting directories

# app = Flask(__name__)

# UPLOAD_FOLDER = 'test'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'post_image' in request.files:
#             file = request.files['post_image']
#             if file.filename != '':
#                 filename = secure_filename('test.jpg')
#                 file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#                 file.save(file_path)

#                 # ลบโฟลเดอร์ "exp" ใน "runs/detect"
#                 exp_folder = 'runs/detect/exp'
#                 if os.path.exists(exp_folder):
#                     shutil.rmtree(exp_folder)

#                 # Call the detection script
#                 command = f'python detect-custom.py --weights wire100e.pt --source test'
#                 # command = f'python detect-custom.py --weights wire20e.pt --source test'
#                 process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
#                 output, _ = process.communicate()

#                 return jsonify({"message": "File uploaded and processed successfully", "output": output.decode('utf-8')})

#     return render_template('upload.html')



# if __name__ == '__main__':
#     app.run()


from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import subprocess
import shutil  # Import shutil for deleting directories

app = Flask(__name__)

UPLOAD_FOLDER = 'test'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'post_image' in request.files:
            file = request.files['post_image']
            if file.filename != '':
                filename = secure_filename('test.jpg')
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # ลบโฟลเดอร์ "exp" ใน "runs/detect"
                exp_folder = 'runs/detect/exp'
                if os.path.exists(exp_folder):
                    shutil.rmtree(exp_folder)
                
                exp_folder = 'yolov7/runs/detect/exp'
                if os.path.exists(exp_folder):
                    shutil.rmtree(exp_folder)

                # Call the detection script
                command = f'python detect-custom.py --weights wire100e.pt --source test --save-crop --save-txt && python yolov7/detect-custom.py --weights yolov7/bestv7-100.pt --conf 0.25 --img-size 640 --source test --save-txt'
                # command = f'python detect-custom.py --weights wire20e.pt --source test --save-crop --save-txt && python yolov7/detect-custom.py --weights yolov7/bestv7-20.pt --conf 0.05 --img-size 640 --source test --save-txt'
                # command = f'python detect-custom.py --weights wire20e.pt --source test'
                # command = f'python yolov7/detect-custom.py --weights yolov7/bestv7-100.pt --conf 0.25 --img-size 640 --source test'
                # command = f'python detect-custom.py --weights wire20e.pt --source test'

                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                output, _ = process.communicate()

                return jsonify({"message": "File uploaded and processed successfully", "output": output.decode('utf-8')})

    return render_template('upload.html')



if __name__ == '__main__':
    app.run()
