%rebase("base.tpl")

    <h1 style="color:rgb(59, 182, 110);">
        {{!base}}
    </h1><br>
        
    <h3 style="color:rgb(255, 38, 0);">
        {{!alert}}
    </h3>

    <h2>
        <form action="/en/upload/" method="post" enctype="multipart/form-data">
            
            <div class="col-sm-9">
                <label for="data">You can upload .txt, .csv or .xlsx file here. Make sure data is written in the first two columns, with no headers in the first row.</label> <br><br>
                <input type="file" name="data" class="form-control form-control-lg" aria-label="file example" required/> <br>
            </div>
            
            <div class="col-sm-2">
                <label for="title">Title</label>
                <input type="text" id="title" name="title" class="form-control"><br>
            </div>
            
            <div class="row">
                <div class="col-sm-2">
                    <label for="x label">x label</label>
                    <input type="text" id="x_label" name="x_label" class="form-control"><br>
                </div>
                <div class="col-sm-2">
                    <label for="y label">y label</label>
                    <input type="text" id="y_label" name="y_label" class="form-control"><br>
                </div>
            </div>


            <label for="fit">Choose a fit:</label>
            <select name="fit" id="fit">
              <optgroup label="polynomial fit">
                <option value="linear">Linear</option>
                <option value="quadratic">Quadratic</option>
                <option value="cubic">Cubic</option>
              </optgroup>

                <option value="exponential">Exponential</option>
                <option value="logarithmic">Logarithmic</option>
                <option value="None">Without fit</option>
            </select><br><br>

            <input type="submit" value='Submit' class="btn btn-success"/>
        </form>
    </h2>