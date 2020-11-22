# 廣韻 for Mac

This project converts 廣韻 data into a format recognizable by Apple Dictionary, so that you can quickly look up the readings. It can serve as a local version of [ytenx](https://ytenx.org).

**Current Version: 0.1**.

## Build and Install

First, download [Additional Tools for Xcode](https://developer.apple.com/download/more/?=for%20Xcode).

Then, run the following commands:

```bash
# Change the path if necessary
make DICT_BUILD_TOOL_DIR="/Volumes/Additional Tools/Utilities/Dictionary Development Kit"

# Install to ~/Library/Dictionaries
make install
```

All done. Enjoy!

## Acknowledgements

This project is a direct derivative work of [poem's 廣韻全字表](https://zhuanlan.zhihu.com/p/20430939).

## TODO and ChangeLog

Version 0.1:

- [x] 反切
- [x] 音韻地位
- [x] 字義

Planned:

- [ ] 界面美化
- [ ] 小韻
- [ ] 反切上字
- [ ] 反切下字
- [ ] 聲紐
- [ ] 韻部
- [ ] 常見拼音方案
- [ ] 域外方音（日、韓、越）

Maybe useful:

- [ ] 按反切、拼音查尋
- [ ] 常用擬音方案
- [ ] 漢字字形演變
- [ ] 上古韻部
- [ ] 詞根與詞族
- [ ] 收錄康熙字典
- [ ] 增加音韻學教程䈎
