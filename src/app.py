import argparse, sys, subprocess
from ultralytics import YOLO

def check_ffmpeg():
    try:
        out = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        return out.returncode == 0
    except FileNotFoundError:
        return False

def selftest():
    ok_ffmpeg = check_ffmpeg()
    try:
        _ = YOLO("yolov8n.pt")   # downloads the tiny model on first run
        ok_yolo = True
    except Exception as e:
        ok_yolo = False
        print(f"YOLO load error: {e}")
    print(f"FFmpeg: {'OK' if ok_ffmpeg else 'MISSING'} | YOLO: {'OK' if ok_yolo else 'FAIL'}")
    return ok_ffmpeg and ok_yolo

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--selftest", action="store_true", help="Check environment")
    args = p.parse_args()

    if args.selftest:
        ok = selftest()
        sys.exit(0 if ok else 1)

    print("👋 Pipeline not wired yet. Run with --selftest to verify env.")

if __name__ == "__main__":
    main()
