Name: pico-imx8mq-bootimage
Version: 4.14.98
Release: alt2

Summary: Combined boot image for TechNexion PICO IMX8MQ board
License: GPL
Group: System/Kernel and hardware

BuildArch: noarch

Source: %name-%version-%release.tar

Patch0: build-shared-binaries.patch
Patch1: do-not-call-git-to-determine-build-number.patch

BuildRequires: uboot-tools zlib-devel dtc
BuildRequires: u-boot-pico-imx8mq
BuildRequires: imx-atf-imx8mq
BuildRequires: firmware-imx

%description
Combined boot image for TechNexion PICO IMX8MQ board

%prep
%setup

%patch0 -p1
%patch1 -p1

%define platform iMX8M
%define board pico-imx8mq

cp %_datadir/u-boot/%{board}/* %platform

cp %_bindir/mkimage %platform/mkimage_uboot

cp %_datadir/atf/imx8mq/bl31.bin %platform

cp /lib/firmware/imx/ddr/synopsys/lpddr4_pmu_train_1d_dmem.bin %platform
cp /lib/firmware/imx/ddr/synopsys/lpddr4_pmu_train_1d_imem.bin %platform
cp /lib/firmware/imx/ddr/synopsys/lpddr4_pmu_train_2d_dmem.bin %platform
cp /lib/firmware/imx/ddr/synopsys/lpddr4_pmu_train_2d_imem.bin %platform
cp /lib/firmware/imx/hdmi/cadence/signed_hdmi_imx8m.bin %platform

%build
%make_build SOC=%platform dtbs=imx8mq-pico-pi.dtb flash_hdmi_spl_uboot

%install
install -pm0644 -D %platform/flash.bin %buildroot%_datadir/pico-imx8mq-bootimage/flash.bin

%files
%_datadir/pico-imx8mq-bootimage

%changelog
* Wed Jul 17 2019 Pavel Nakonechnyi <zorg@altlinux.org> 4.14.98-alt2
- make target package noarch

* Sun Jul 07 2019 Pavel Nakonechnyi <zorg@altlinux.org> 4.14.98-alt1
- initial build of bootimage for TechNexion PICO IMX8MQ board
