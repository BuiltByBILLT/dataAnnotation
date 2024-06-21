<?php
function resizeImage($sourcePath, $destPath, $newWidth, $newHeight) {
    // Get original image dimensions and type
    list($origWidth, $origHeight, $imageType) = getimagesize($sourcePath);

    // Choose creation function based on image type
    switch ($imageType) {
        case IMAGETYPE_JPEG:
            $image = imagecreatefromjpeg($sourcePath);
            break;
        case IMAGETYPE_PNG:
            $image = imagecreatefrompng($sourcePath);
            break;
        case IMAGETYPE_GIF:
            $image = imagecreatefromgif($sourcePath);
            break;
        default:
            throw new Exception("Unsupported image type");
    }

    // Create new image resource
    $newImage = imagecreatetruecolor($newWidth, $newHeight);

    // Maintain image transparency (for PNGs, GIFs)
    if ($imageType == IMAGETYPE_PNG || $imageType == IMAGETYPE_GIF) {
        imagecolortransparent($newImage, imagecolorallocatealpha($newImage, 0, 0, 0, 127));
        imagealphablending($newImage, false);
        imagesavealpha($newImage, true);
    }

    // Resize
    imagecopyresampled($newImage, $image, 0, 0, 0, 0, $newWidth, $newHeight, $origWidth, $origHeight);

    // Save image
    switch ($imageType) {
        case IMAGETYPE_JPEG:
            imagejpeg($newImage, $destPath, 85); // Adjust quality as needed
            break;
        case IMAGETYPE_PNG:
            imagepng($newImage, $destPath);
            break;
        case IMAGETYPE_GIF:
            imagegif($newImage, $destPath);
            break;
    }

    // Free resources
    imagedestroy($image);
    imagedestroy($newImage);
}

// Test the function
try {
    resizeImage('source200x300.jpg', 'dest.jpg', 200, 200); // Adjust source path, destination path, and size as needed
    echo "Image resized successfully.";
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>