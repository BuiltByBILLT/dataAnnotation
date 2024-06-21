package com.example.mycomposeapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import com.example.mycomposeapp.ui.theme.MyComposeAppTheme


import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.ui.Alignment
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

import android.content.Context
import android.graphics.Bitmap
import android.graphics.Canvas
import android.view.View
import androidx.compose.ui.platform.ComposeView
import androidx.compose.ui.unit.Dp
import java.io.FileOutputStream

import java.io.File


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            MyComposeAppTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    MyComposable()
                }
            }
        }
    }
}



@Composable
fun MyComposable() {
    // Your composable content here
    Box(
        modifier = Modifier
            .size(200.dp)
            .background(Color.Blue)
    ) {
        Text(
            text = "Hello, World!",
            color = Color.White,
            modifier = Modifier.align(Alignment.Center)
        )
    }
}

@Composable
fun renderComposableToBitmap(context: Context, width: Int, height: Int, composable: @Composable () -> Unit): Bitmap {
    val composeView = ComposeView(context).apply {
        setContent {
            composable()
        }
    }

    composeView.measure(
        View.MeasureSpec.makeMeasureSpec(width, View.MeasureSpec.EXACTLY),
        View.MeasureSpec.makeMeasureSpec(height, View.MeasureSpec.EXACTLY)
    )
    composeView.layout(0, 0, composeView.measuredWidth, composeView.measuredHeight)

    val bitmap = Bitmap.createBitmap(composeView.measuredWidth, composeView.measuredHeight, Bitmap.Config.ARGB_8888)
    val canvas = Canvas(bitmap)
    composeView.draw(canvas)

    return bitmap
}

fun saveBitmapAsPng(bitmap: Bitmap, file: File) {
    FileOutputStream(file).use { out ->
        bitmap.compress(Bitmap.CompressFormat.PNG, 100, out)
    }
}

@Composable
fun exportComposableToPngFile(context: Context, file: File) {
    val width = 200.dp.toPx(context).toInt()
    val height = 200.dp.toPx(context).toInt()

    val bitmap = renderComposableToBitmap(context, width, height) {
        MyComposable()
    }

    saveBitmapAsPng(bitmap, file)
}

// Extension function to convert dp to pixels
fun Dp.toPx(context: Context): Float {
    return this.value * context.resources.displayMetrics.density
}