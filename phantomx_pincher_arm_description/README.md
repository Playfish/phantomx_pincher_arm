# phantomx_pincher_arm_description

<h2>Description</h2>

Note: When only use description for Gazebo should do under modify:
Change attribute with joint with base_link otherwise will cause model in gazebo shaking.
In ```urdf/arm_hardware.xacro```
Comment:
```
       <inertial>
       <mass value="0.055"/>
        <origin xyz="0 0 0"/>
        <inertia ixx="0.000017012" ixy="0.0" ixz="0.0"
                 iyy="0.000013258" iyz="0.0"
                 izz="0.000009483"/>
      </inertial>
```
And with instead uncomment:
```
      <!--<inertial>
        <mass value="6.39321" />
        <inertia ixx="0.04593" ixy="-0.00259" ixz="-3e-05"
                 iyy="0.03667" iyz="-0.00031" 
                 izz="0.04858" />
      </inertial>-->
```
