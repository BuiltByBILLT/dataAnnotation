<?php
function resizeImage($filename, $newWidth, $newHeight, $maintainAspectRatio = true) {
    // Get image dimensions and type
    list($originalWidth, $originalHeight, $imageType) = getimagesize($filename);

    // Calculate new dimensions while maintaining aspect ratio (if enabled)
    if ($maintainAspectRatio) {
        $ratio = min($newWidth / $originalWidth, $newHeight / $originalHeight);
        $newWidth = $originalWidth * $ratio;
        $newHeight = $originalHeight * $ratio;
    }

    // Create new image resource
    $newImage = imagecreatetruecolor($newWidth, $newHeight);

    // Load original image based on its type
    switch ($imageType) {
        case IMAGETYPE_JPEG:
            $originalImage = imagecreatefromjpeg($filename);
            break;
        case IMAGETYPE_PNG:
            $originalImage = imagecreatefrompng($filename);
            imagealphablending($newImage, false);
            imagesavealpha($newImage, true);
            break;
        case IMAGETYPE_GIF:
            $originalImage = imagecreatefromgif($filename);
            break;
        default:
            return false; // Unsupported image type
    }

    // Resize and resample the image
    imagecopyresampled($newImage, $originalImage, 0, 0, 0, 0, $newWidth, $newHeight, $originalWidth, $originalHeight);

    // Save the new image
    switch ($imageType) {
        case IMAGETYPE_JPEG:
            imagejpeg($newImage, $filename, 90); // Adjust quality (0-100) as needed
            break;
        case IMAGETYPE_PNG:
            imagepng($newImage, $filename);
            break;
        case IMAGETYPE_GIF:
            imagegif($newImage, $filename);
            break;
    }

    // Free up memory
    imagedestroy($originalImage);
    imagedestroy($newImage);

    return true;
}

$filename = 'sourceAfter.jpg';
$newWidth = 200;
$newHeight = 200;

if (resizeImage($filename, $newWidth, $newHeight)) {
    echo "Image resized successfully!";
} else {
    echo "Image resizing failed.";
}
       

?>