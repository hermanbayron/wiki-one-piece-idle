from pathlib import Path
import sys

import cv2


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python tools/extract_video_frames.py <video> <output-dir> [seconds-step]")
        return 2

    video_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    step_seconds = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0

    if not video_path.exists():
        print(f"Video not found: {video_path}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"Could not open video: {video_path}")
        return 1

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    duration = frame_count / fps if fps else 0
    step_frames = max(1, int(fps * step_seconds))

    saved = 0
    frame_index = 0
    while frame_index < frame_count:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ok, frame = cap.read()
        if not ok:
            break

        timestamp = frame_index / fps
        out_name = f"frame_{saved + 1:03d}_{timestamp:06.2f}s.jpg"
        out_path = output_dir / out_name
        cv2.imwrite(str(out_path), frame)

        saved += 1
        frame_index += step_frames

    cap.release()
    print(f"fps={fps:.2f}")
    print(f"frames={frame_count}")
    print(f"duration={duration:.2f}s")
    print(f"saved={saved}")
    print(f"output={output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
