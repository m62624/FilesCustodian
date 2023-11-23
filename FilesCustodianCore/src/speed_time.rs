use byte_unit::Byte;
use home::home_dir;
use std::fs;
use std::fs::File;
use std::io::{Result, Write};
use std::time::Instant;
use sys_info::disk_info;
use uuid::Uuid;

#[derive(Debug)]
pub enum WriteSpeed {
    KilobytesPerSecond(f64),
    MegabytesPerSecond(f64),
    GigabytesPerSecond(f64),
}

impl WriteSpeed {
    fn from_bytes_per_second(bytes_per_second: f64) -> WriteSpeed {
        if bytes_per_second < 1024.0 {
            WriteSpeed::KilobytesPerSecond(bytes_per_second)
        } else if bytes_per_second < 1024.0 * 1024.0 {
            WriteSpeed::MegabytesPerSecond(bytes_per_second / 1024.0)
        } else {
            WriteSpeed::GigabytesPerSecond(bytes_per_second / (1024.0 * 1024.0))
        }
    }
}

fn check_disk_space() -> Result<f64> {
    if let Ok(disk) = disk_info() {
        let free_gb = disk.free as f64 / (1024.0 * 1024.0);
        println!("Свободно {} GB на диске.", free_gb);
        match free_gb < 1.0 {
            true => {
                return Err(std::io::Error::new(
                    std::io::ErrorKind::Other,
                    "На диске недостаточно места.",
                ))
            }
            false => Ok(free_gb),
        }
    } else {
        return Err(std::io::Error::new(
            std::io::ErrorKind::Other,
            "Не удалось получить информацию о диске.",
        ));
    }
}

pub fn measure_write_speed() -> Result<(f64, WriteSpeed)> {
    // Генерируем UUID

    // Определяем home директорию
    let home_dir = match home_dir() {
        Some(path) => path,
        None => {
            return Err(std::io::Error::new(
                std::io::ErrorKind::Other,
                "Не удалось определить домашнюю директорию.",
            ))
        }
    };
    let free = check_disk_space()?;
    let data_size_gb = (free * (5 as f64 / 100.0)).floor();
    println!("data size gb {}", data_size_gb);
    // Создаем временную директорию
    let name = format!("temp-{}", Uuid::new_v4().hyphenated());
    let tmp_dir = home_dir.join(name);
    println!("Создаем временную директорию: {:?}", tmp_dir);
    fs::create_dir_all(&tmp_dir)?;

    // Создаем временный файл для записи данных
    let data_size_bytes = (data_size_gb * 1024.0 * 1024.0 * 1024.0).round() as u64;
    let data_file_path = tmp_dir.join("data.bin");

    // Проверяем место на диске

    let mut file = File::create(&data_file_path)?;

    let start_time = Instant::now();

    // Записываем данные на диск
    let data = vec![0u8; data_size_bytes as usize];
    file.write_all(&data)?;

    let elapsed_time = start_time.elapsed();
    let elapsed_seconds = elapsed_time.as_secs() as f64 + elapsed_time.subsec_nanos() as f64 / 1e9;
    let write_speed = (data_size_bytes as f64 / 1024.0) / elapsed_seconds; // KB/s
    // fs::remove_dir_all(&tmp_dir)?;
    Ok((
        elapsed_seconds,
        WriteSpeed::from_bytes_per_second(write_speed),
    ))
}
