from ij import IJ

#@ String (label="Please enter the input directory", description="Input Directory") inDir
#@ String (label="Please enter the output directory", description="Input Directory") outDir
#@ String (label="Please enter the expected overlap", description="Overlap") overlap

IJ.run("Grid/Collection stitching", "type=[Grid: row-by-row] order=[Right & Down                ] grid_size_x=2 grid_size_y=2 tile_overlap=" + overlap + " first_file_index_i=1 directory=" 
        + inDir + " file_names={i}.jpg output_textfile_name=TileConfiguration.txt fusion_method=[Linear Blending] regression_threshold=0.70 max/avg_displacement_threshold=2.5 "
        + "absolute_displacement_threshold=3.5 compute_overlap subpixel_accuracy computation_parameters=[Save computation time (but use more RAM)] image_output=[Fuse and display]");
IJ.saveAs("Jpeg", outDir);
